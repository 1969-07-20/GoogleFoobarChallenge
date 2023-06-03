import os
import sys
import json
import argparse
import importlib
from copy import deepcopy
from math import log, ceil, floor

#  Version info
version_num = '0.1.1'
version_date = '2023-05-31a'

version = 'version %s (%s)' % (version_num, version_date)


#  From:  https://stackoverflow.com/questions/34803467/unexpected-exception-name-basestring-is-not-defined-when-invoking-ansible2
try:
  basestring
except NameError:
  basestring = str


try:
    import tracemalloc
    trace_malloc_loaded = True
except ImportError as error:
    trace_malloc_loaded = False


have_timer0 = False
have_timer1 = False
try:
    from time import perf_counter_ns
    have_timer0 = True
except ImportError as error:
    try:
        import time
        have_timer1 = True
    except ImportError as error:
        print("Unable to import timer.  Timing info will not be reported.")


#  From https://stackoverflow.com/questions/616645/how-to-duplicate-sys-stdout-to-a-log-file (Status)

class Logger(object):
    "Lumberjack class - duplicates sys.stdout to a log file and it's okay"
    #source: https://stackoverflow.com/q/616645
    def __init__(self, filename="Red.Wood", mode="ab", buff=0):
        self.stdout = sys.stdout
        self.file = open(filename, mode, buff)
        sys.stdout = self

    def __del__(self):
        self.close()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.close()

    def write(self, message):
        self.stdout.write(message)
        #elf.file.write(message)
        self.file.write(message.encode("utf-8"))

    def flush(self):
        self.stdout.flush()
        self.file.flush()
        os.fsync(self.file.fileno())

    def close(self):
        if self.stdout != None:
            sys.stdout = self.stdout
            self.stdout = None

        if self.file != None:
            self.file.close()
            self.file = None




extern_modules = {}

try:
    import numpy as np
    extern_modules['numpy'] = True
except ImportError as error:
    print("IMPORT ERROR:  numpy")


def check_dependencies(dep_list):

    #  Loop over dependencies in dependency list
    for dep in dep_list:

        #  Ensure the dependency is a string
        if isinstance(dep, str) or sys.version_info[0] < 3 and isinstance(dep, basestring):
            pass
        else:
            return False

        #  Ensure the dependency is in the list of external modules
        if dep not in extern_modules:
            return False

    #  No dependency failed so dependencies are satisfied
    return True


def timeout_NoOp(*dummy_args):
    pass

def timeout(func, args=(), kwargs=None, timeout_sec=60, default=None):
    import signal

    class TimeoutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeoutError()

    # set the timeout handler
    kwargs = kwargs or {}

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_sec)
    try:
        result = func(*args, **kwargs)
        timed_out = False
    except TimeoutError as exc:
        result = default
        timed_out = True
    finally:
        signal.alarm(0)

    return (result, timed_out)


#  From:  https://stackoverflow.com/questions/8790003/dynamically-import-a-method-in-a-file-from-a-string
def load_solution(solution):
    """
    dynamically load solution module specified in the string
    """

    #  Parse the module string
    module_path = solution['file']

    solution['module_name'] = module_path.split(".")[-1]

    if ('dep' in solution):

        #  Get dependencies as a list
        if isinstance(solution['dep'], list):
            deps = solution['dep']
        else:
            deps = [solution['dep']]

        #  Check dependencies
        if not check_dependencies(deps):
            solution['function'] = None
            solution['source_url'] = '<UNKNOWN>'

            return

    #  Load the module
    module = importlib.import_module(module_path)

    #  Get the module components that will be used later

    #  Retrieve the url to the source of the solution
    try:
        solution['source_url'] = getattr(module, 'source_url')
    except Exception as ex:
        solution['source_url'] = '<UNKNOWN>'

        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    #  Finally, retrieve the main function
    try:
        solution['function'] = getattr(module, solution['entry'])
    except Exception as ex:
        solution['function'] = None

        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    return


def plot_outcomes(outcomes, idx_case, do_time, do_memory):
    num_spaces = 60

    log_neg_lim = -4
    log_pos_lim = 4


    if do_time:

        min_time = float('+inf')
        max_time = float('-inf')

        times = []

        for outcome in outcomes:

            if None is not outcome['time_in_s']:
               if min_time > outcome['time_in_s']:
                   min_time = outcome['time_in_s']

               if max_time < outcome['time_in_s']:
                   max_time = outcome['time_in_s']

               times.append(outcome['time_in_s'])

        times.sort()

        half_len_times = len(times) // 2

        if len(times) > (half_len_times + half_len_times):
           med_time = times[half_len_times]
        else:
           med_time = (times[half_len_times - 1] + times[half_len_times]) / 2.0

        if min_time <= 0.0:
           log_min = log_neg_lim
        else:
           log_min = log(min_time / med_time) / log(2)
        log_max = log(max_time / med_time) / log(2)

        log_neg = int(-ceil(-log_min))
        log_pos = int( ceil( log_max))

        if log_neg < log_neg_lim:
            log_neg = log_neg_lim

        if log_pos > log_pos_lim:
            log_pos = log_pos_lim


        print('')
        print('')
        print('LOG SCALE (BASE 2) PLOT OF RATIO OF SOLUTION EXECUTION TIME TO MEDIAN EXECUTIION TIME (%.2e sec) FOR TEST CASE %d' % (med_time, idx_case))
        print('')
        print('                        Time /')
        print(' SOLUTION    Time (s)   Median')
        print(' ---------   --------   --------     <-- FASTER' + ' '*(num_spaces-20) + 'SLOWER -->')

        for outcome in outcomes:
            time_in_s = outcome['time_in_s']

            if None is not time_in_s:
                val_next = (2.0**log_neg) * med_time

                val_inc = float(log_pos - log_neg) / float(num_spaces - 1)

                line = ''

                for idx in range(num_spaces):
                    val = val_next

                    val_next = (2.0**(log_neg + (idx + 1) * val_inc)) * med_time

                    if time_in_s < med_time:
                        if val_next < time_in_s:
                            line = line + ' '
                        elif (val <= time_in_s) and (time_in_s < val_next):
                            line = line + '+'
                        elif (val_next < med_time):
                            line = line + '-'
                        elif (val <= med_time) and (med_time < val_next):
                            line = line + '|'
                        else:
                            line = line + ' '
                    else:
                        if time_in_s < val:
                            line = line + ' '
                        elif (val <= time_in_s) and (time_in_s < val_next):
                            line = line + '+'
                        elif (med_time < val):
                            line = line + '-'
                        elif (val <= med_time) and (med_time < val_next):
                            line = line + '|'
                        else:
                            line = line + ' '

                if time_in_s > (2**log_pos) * med_time:
                   line = line[:-2] + '>>'

                if time_in_s < (2**log_neg) * med_time:
                   line = '<<' + line[2:]


                line = list(line)

                for pow in range(log_neg, log_pos+1):
                    loc = int((num_spaces - 1) * (pow - log_neg) / (log_pos - log_neg))

                    if ' ' == line[loc]:
                        line[loc] = '.'

                line = ''.join(line)

            else:
                line = list(' '*num_spaces)

                for pow in range(log_neg, log_pos+1):
                    loc = int((num_spaces - 1) * (pow - log_neg) / (log_pos - log_neg))

                    line[loc] = '.'

                line = ''.join(line)


            if time_in_s is not None:
                print('%10s:  %.2e   %.2e     %s' % (outcome['solution'], time_in_s, time_in_s / med_time, line))
            else:
                print('%10s:  --------   --------     %s' % (outcome['solution'], line))


        #  Add ticks to log scale
        line0 = list(' ' * num_spaces)
        line1 = list(' ' * num_spaces)
        line2 = list(' ' * num_spaces)

        for pow in range(log_neg, log_pos+1):
            loc = int((num_spaces - 1) * (pow - log_neg) / (log_pos - log_neg))

            if 0 > pow:
                char0 = '/'

                val = int(round(2**(-pow)))
            else:
                char0 = 'x'

                val = int(round(2**(pow)))

            if 10 >= val:
                char1 = str(val)
                char2 = ' '
            else:
                char1 = str(val // 10)
                char2 = str(val % 10)

            line0[loc] = char0
            line1[loc] = char1
            line2[loc] = char2

        print('                                     %30s' % (''.join(line0)))
        print('                                     %30s' % (''.join(line1)))
        print('                                     %30s' % (''.join(line2)))


    if do_memory:

        #  Process peak memory allocation
        min_size = float('+inf')
        max_size = float('-inf')

        sizes = []

        for outcome in outcomes:

            if None is not outcome['tm_peak']:
               if min_size > outcome['tm_peak']:
                   min_size = outcome['tm_peak']

               if max_size < outcome['tm_peak']:
                   max_size = outcome['tm_peak']

               sizes.append(outcome['tm_peak'])

        sizes.sort()

        half_len_sizes = len(sizes) // 2

        if len(sizes) > (half_len_sizes + half_len_sizes):
           med_size = sizes[half_len_sizes]
        else:
           med_size = (sizes[half_len_sizes - 1] + sizes[half_len_sizes]) / 2.0

        if min_size <= 0.0:
           log_min = log_neg_lim
        else:
           log_min = log(min_size / med_size) / log(2)
        log_max = log(max_size / med_size) / log(2)

        log_neg = int(-ceil(-log_min))
        log_pos = int( ceil( log_max))

        if log_neg < log_neg_lim:
            log_neg = log_neg_lim

        if log_pos > log_pos_lim:
            log_pos = log_pos_lim


        print('')
        print('')
        print('LOG SCALE (BASE 2) PLOT OF RATIO OF SOLUTION PEAK MEMORY USAGE TO MEDIAN PEAK MEMORY USAGE (%.2e kb) FOR TEST CASE %d' % (med_size, idx_case))
        print('')
        print('                         Peak /')
        print(' SOLUTION    Peak (kb)   Median')
        print(' ---------   ---------   --------     <-- ECONOMICAL' + ' '*(num_spaces-26) + 'WASTEFUL -->')

        for outcome in outcomes:
            tm_peak = outcome['tm_peak']

            if None is not tm_peak:
                val_next = (2.0**log_neg) * med_size

                val_inc = float(log_pos - log_neg) / float(num_spaces - 1)

                line = ''

                for idx in range(num_spaces):
                    val = val_next

                    val_next = (2.0**(log_neg + (idx + 1) * val_inc)) * med_size

                    if tm_peak < med_size:
                        if val_next < tm_peak:
                            line = line + ' '
                        elif (val <= tm_peak) and (tm_peak < val_next):
                            line = line + '+'
                        elif (val_next < med_size):
                            line = line + '-'
                        elif (val <= med_size) and (med_size < val_next):
                            line = line + '|'
                        else:
                            line = line + ' '
                    else:
                        if tm_peak < val:
                            line = line + ' '
                        elif (val <= tm_peak) and (tm_peak < val_next):
                            line = line + '+'
                        elif (med_size < val):
                            line = line + '-'
                        elif (val <= med_size) and (med_size < val_next):
                            line = line + '|'
                        else:
                            line = line + ' '

                if tm_peak > (2**log_pos) * med_size:
                   line = line[:-2] + '>>'

                if tm_peak < (2**log_neg) * med_size:
                   line = '<<' + line[2:]


                line = list(line)

                for pow in range(log_neg, log_pos+1):
                    loc = int((num_spaces - 1) * (pow - log_neg) / (log_pos - log_neg))

                    if ' ' == line[loc]:
                        line[loc] = '.'

                line = ''.join(line)

            else:
                line = list(' '*num_spaces)

                for pow in range(log_neg, log_pos+1):
                    loc = int((num_spaces - 1) * (pow - log_neg) / (log_pos - log_neg))

                    line[loc] = '.'

                line = ''.join(line)


            if tm_peak is not None:
                print('%10s:  %.2e    %.2e     %s' % (outcome['solution'], tm_peak, tm_peak / med_size, line))
            else:
                print('%10s:  --------    --------     %s' % (outcome['solution'], line))



        #  Add ticks to log scale
        line0 = list(' ' * num_spaces)
        line1 = list(' ' * num_spaces)
        line2 = list(' ' * num_spaces)

        for pow in range(log_neg, log_pos+1):
            loc = int((num_spaces - 1) * (pow - log_neg) / (log_pos - log_neg))

            if 0 > pow:
                char0 = '/'

                val = int(round(2**(-pow)))
            else:
                char0 = 'x'

                val = int(round(2**(pow)))

            if 10 >= val:
                char1 = str(val)
                char2 = ' '
            else:
                char1 = str(val // 10)
                char2 = str(val % 10)

            line0[loc] = char0
            line1[loc] = char1
            line2[loc] = char2

        print('                                      %30s' % (''.join(line0)))
        print('                                      %30s' % (''.join(line1)))
        print('                                      %30s' % (''.join(line2)))


def print_version(version):
    print('OfflineTester:  %s' % (version))


#  Adapted from:  https://github.com/symonsoft/str2bool/blob/master/str2bool/__init__.py
def loc_strtobool(value, raise_exc=False):
    _true_set = {'yes', 'true', 't', 'y', '1'}
    _false_set = {'no', 'false', 'f', 'n', '0'}

    if isinstance(value, str) or sys.version_info[0] < 3 and isinstance(value, basestring):
        value = value.lower()
        if value in _true_set:
            return True
        if value in _false_set:
            return False

    if raise_exc:
        raise ValueError('Expected "%s"' % '", "'.join(_true_set | _false_set))
    return None


def init_argparse():
    parser = argparse.ArgumentParser(
#       usage="%(prog)s [OPTION] [FILE]...",
        description="Run Foobar solutions against test cases.",
    )
    parser.add_argument( "-v", "--version", action="version", version="%s %s" % (parser.prog, version))

    parser.add_argument('--challenge', default='ALL', help='challenge to run')
    parser.add_argument('--do_trace_malloc', default=True, dest='do_trace_malloc', metavar='<True|False>', type=lambda x:bool(loc_strtobool(x)))
    parser.add_argument('--do_short_output', default=False, dest='do_short_output', metavar='<True|False>', type=lambda x:bool(loc_strtobool(x)))
    parser.add_argument('--do_debug_exception', default=False, dest='do_debug_exception', metavar='<True|False>', type=lambda x:bool(loc_strtobool(x)))
    parser.add_argument('--do_print_to_log', default=False, dest='do_print_to_log', metavar='<True|False>', type=lambda x:bool(loc_strtobool(x)))
    parser.add_argument('--timeout_sec', default=5, dest='timeout_sec', type=int)
    parser.add_argument('--timing_duration', default=0.5, dest='timing_duration', type=float)

    return parser


def main():

    #  Parse command line arguments
    arg_parser = init_argparse()

    args = arg_parser.parse_args()


    #  Extract commandline arguments to variables used during execution
    if ('challenge' in args) and (args.challenge is not None):
        if 'ALL' == args.challenge.upper():
            challenges = [
                "Level1_BrailleTranslation",
                "Level1_ILoveLanceAndJanice",
                "Level1_MinionWorkAssignments",
                "Level1_Re-ID",
                "Level1_SkippingWork_aka_PrisonLaborDodgers",
                "Level1_SolarDoomsday",
                "Level1_TheCakeIsNotALie",
                "Level2_BunnyWorkerLocations",
                "Level2_DontGetVolunteered",
                "Level2_ElevatorMaintenance",
                "Level2_EnRouteSalute",
                "Level2_GearingUpForDestruction",
                "Level2_HeyIAlreadyDidThat",
                "Level2_IonFluxRelabeling",
                "Level2_NumbersStationCodedMessages",
                "Level2_PleasePassTheCodedMessages",
                "Level2_PowerHungry",
                "Level3_BombBaby",
                "Level3_DoomsdayFuel",
                "Level3_FindTheAccessCodes",
                "Level3_FuelInjectionPerfection",
                "Level3_PrepareTheBunniesEscape",
                "Level3_QueueToDo",
                "Level3_TheGrandestStaircaseOfThemAll",
                "Level4_BringingAGunToATrainerFight",
                "Level4_DistractTheGuards",
                "Level4_EscapePods",
                "Level4_FreeTheBunnyWorkers",
                "Level4_RunningWithBunnies",
                "Level5_DisorderlyEscape",
                "Level5_DodgeTheLasers",
                "Level5_ExpandingNebula",
            ]
        else:
           challenges = args.challenge.split(',')

    if ('do_trace_malloc' in args) and (args.do_trace_malloc is not None):
        do_trace_malloc = args.do_trace_malloc and trace_malloc_loaded
    else:
        do_trace_malloc = True and trace_malloc_loaded

    if ('do_short_output' in args) and (args.do_short_output is not None):
        do_short_output = args.do_short_output
    else:
        do_short_output = True

    if ('do_debug_exception' in args) and (args.do_debug_exception is not None):
        do_debug_exception = args.do_debug_exception
    else:
        do_debug_exception = False

    if ('do_print_to_log' in args) and (args.do_print_to_log is not None):
        do_print_to_log = args.do_print_to_log
    else:
        do_print_to_log = False

    if ('timeout_sec' in args) and (args.timeout_sec is not None):
        timeout_sec = args.timeout_sec
    else:
        timeout_sec = 5

    if ('timing_duration' in args) and (args.timing_duration is not None):
        timing_duration = args.timing_duration
    else:
        timing_duration = 0.5


    #  Process challenges one at a time
    for challenge in challenges:

        #  Open log
        if do_print_to_log:
            log_file = 'testResults_' + challenge + '.txt'
            Log=Logger(log_file)


        #  Print out version
        print_version(version)

        #  Print challenge name
        print('')
        print('Challenge:  %s' % challenge)


        #  Read in the JSON file with info about the solutions
        with open(challenge + os.sep + 'solutions.json') as user_file:
            solutions = json.load(user_file)


        #  Read in the JSON file with info about the test cases
        with open(challenge + os.sep + 'testCases.json') as user_file:
            test_cases = json.load(user_file)


        #  Print out test cases
        print('')
        print('')

        idx_case = 0
        for test_case in test_cases:
            print('')
            print('TEST CASE %d:' % (idx_case))
            print('       Description:  %s' % (test_case['desc']))
            print('  Test case source:  %s' % (test_case['source']))
            print('             Input:  %s' % (str(test_case['input'])))
            print('    Correct output:  %s' % (test_case['output']))

            idx_case += 1


        #  Load the modules
        print('Loading solutions')

        idx_sol = 0
        for solution in solutions:
            load_solution(solution)

            solution['idx'] = idx_sol
            idx_sol += 1


        #  Print info about each solution
        print('')
        print('')
        print('SOLUTIONS')
        for solution in solutions:
            if None is solution['function']:
                result = 'FAILED'
            else:
                result = 'LOADED'

            print('%s:  Status:  %s  Source:  %s ' % (solution['module_name'], result, solution['source_url']))


        #  Perform tests
        idx_case = 0
        for test_case in test_cases:
            print('')
            print('')
            print('============================================')
            print('TEST CASE %d:' % (idx_case))
            print('============================================')
            print('')
            print('             Input:  %s' % (str(test_case['input'])))
            print('    Correct output:  %s' % (test_case['output']))
            print('')


            #  Measure overhead
            if (have_timer0 or have_timer1) and (0.0 < timeout_sec):
                for _ in range(2):
                    num_iterations = 0

                    if have_timer0:
                        start = perf_counter_ns()
                    else:
                        start = time.time()

                    while True:
                        num_iterations += 1

                        #  Make a copy of the input data
                        try:
                            input = deepcopy(test_case['input'])
                        except Exception as ex:
                            raise SystemExit('Deepcopy failed.  ABORTING')

                        #  Run a NoOp function
                        timeout(timeout_NoOp,
                                args=input, kwargs=None,
                                timeout_sec=timeout_sec)


                        #  Determine how long that took
                        if have_timer0:
                            end = perf_counter_ns()
                            time_in_s = (end - start) / 1000000000.0
                        else:
                            end = time.time()
                            time_in_s = (end - start) * 1.0


                        #  Break if we have exceeded the timing duration
                        if timing_duration < time_in_s:
                            overhead_in_s = time_in_s / num_iterations
                            break
            else:
                overhead_in_s = 0.0


            #  Run the solutions against the test case
            outcomes = []

            for solution in solutions:
                if None is not solution['function']:

                    #  Initialize the timer
                    num_iterations = 0

                    if have_timer0:
                        start = perf_counter_ns()
                    elif have_timer1:
                        start = time.time()

                    #  Repeatedly run the solution until sufficient time has elapsed
                    while True:
                        num_iterations += 1

                        try:
                            #  Make a copy of the input data
                            try:
                                input = deepcopy(test_case['input'])
                            except Exception as ex:
                                raise SystemExit('Deepcopy failed.  ABORTING')

                            #  Run the solution
                            if 0.0 < timeout_sec:
                                output, timed_out = timeout(solution['function'],
                                    args=input, kwargs=None,
                                    timeout_sec=timeout_sec)
                            else:
                                output = solution['function'](*input)
                                timed_out = False

                        except Exception as ex:
                            output = None

                            if do_debug_exception:
                                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                                message = template.format(type(ex).__name__, ex.args)
                            else:
                                message = "ERROR:  Caught exception.  Execution of '%s' ABORTED." % solution['module_name']

                            print(message)


                        #  Determine how long that took
                        if timed_out:
                            time_in_s = None
                        elif have_timer0:
                            end = perf_counter_ns()
                            time_in_s = (end - start) / 1000000000.0
                        elif have_timer1:
                            end = time.time()
                            time_in_s = (end - start) * 1.0
                        else:
                            time_in_s = None


                        #  Break if not measuring execution time
                        if time_in_s is None:
                            break

                        #  Break if we have exceeded the timing duration
                        if timing_duration < time_in_s:
                            time_in_s /= num_iterations
                            break

                        #  Break if no answer was produced (due to execution aborted due to exception)
                        if output is None:
                            break

                    #  Check to see if the correct answer was produced
                    if timed_out:
                        result = 'TIMEOUT '
                    elif output == test_case['output']:
                        result = 'pass    '
                    else:
                        result = 'FAIL <--'


                    #  Default tracemalloc statistics
                    tm_leak = None
                    tm_peak = None

                    #  If requested run solution one time to trace memory usage
                    if do_trace_malloc and output is not None:
                        try:
                           input = deepcopy(test_case['input'])
                        except Exception as ex:
                           raise SystemExit('Deepcopy failed.  Exiting')

                        tracemalloc.start()
                        tm_size_beg, tm_peak_beg = tracemalloc.get_traced_memory()

                        try:
                            solution['function'](*input)
                        except Exception as ex:
                            pass

                        tm_size_end, tm_peak_end = tracemalloc.get_traced_memory()
                        tracemalloc.stop()

                        tm_leak = (tm_size_end - tm_size_beg) / 1000.0
                        tm_peak = (tm_peak_end - tm_size_beg) / 1000.0
                    else:
                        tm_leak = None
                        tm_peak = None

                    #  Record statistics
                    outcomes.append({
                        'solution':    solution['module_name'],
                        'time_in_s':   time_in_s,
                        'tm_leak':     tm_leak,
                        'tm_peak':     tm_peak,
                    })


                    #  Print result of running current solution on current test case
                    if do_short_output:
                        if None is not time_in_s:
                            if None is not tm_peak:
                                print('  %s:  %s   %s  (%.2e sec)  (%.1e kb)' % (solution['module_name'], result, str(output), time_in_s - overhead_in_s, tm_peak))
                            else:
                                print('  %s:  %s   %s  (%.2e sec)'            % (solution['module_name'], result, str(output), time_in_s - overhead_in_s))
                        else:
                            if None is not tm_peak:
                                print('  %s:  %s   %s              (%.1e kb)' % (solution['module_name'], result, str(output),                            tm_peak))
                            else:
                                print('  %s:  %s   %s'                        % (solution['module_name'], result, str(output)))

                    else:
                        print('  %s:  %s   %s' % (solution['module_name'], result, str(output)))
                else:
                    print('  %s:  SKIP       ---' % (solution['module_name']))


            #  Process the metrics for the test case
            if not do_short_output:
                plot_outcomes(outcomes, idx_case, (have_timer0 or have_timer1), do_trace_malloc)


            idx_case += 1

        if do_print_to_log:
            Log.close()


if __name__ == '__main__':
    main()
