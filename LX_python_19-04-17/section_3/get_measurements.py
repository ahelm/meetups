from subprocess import run, PIPE
from pathlib import Path
from find_tags import find_tags

arr_length = [2 ** i for i in range(6, 18)]
CWD = Path(__file__).parent.resolve()

# execute C program
c_timings = []

print("running C tests ... ", end="", flush=True)
for l in arr_length:
    print(f"{l} ... ", end="", flush=True)
    c_run = run([CWD / "find_tags", str(l)], stdout=PIPE)

    if c_run.returncode:
        raise RuntimeError("C program gave wrong error code")
    c_timings.append(float(c_run.stdout.strip().decode("utf-8")))
print("done", flush=True)

# execute Python code

py_timings = []
int main(int argc, char const *argv[])
{
  if (argc != 2)
  {
    printf("An array size is required and not more or less!\n");
    return 1;
  }

  int array_len = strtoumax(argv[1], NULL, 10); // length of the two arrays
  int *arr1 = malloc(array_len * sizeof(int));  // has all the correct tags
  int *arr2 = malloc(array_len * sizeof(int));  // can have tags from arr1 and others
  int count;                                    // counter for common tags

  init_array(arr1, arr2, array_len, &count);

  shuffle_array(arr1, array_len);
  shuffle_array(arr2, array_len);

  int check;
  clock_t tic, toc;

  tic = clock();
  check = count_common_entries(arr1, arr2, array_len);
  toc = clock();

  // print time in ms
  printf("%.2f\n", 1000.0 * (toc - tic) / CLOCKS_PER_SEC);

  // deallocate the arrays
  free(arr1);
  free(arr2);

  if (check != count)
  {
    return -1;
  }
  else
  {
    return 0;
  }
}
print("running python tests ... ", end="", flush=True)
for l in arr_length:
    print(f"{l} ... ", end="", flush=True)
    py_timings.append(find_tags(l))
print("done", flush=True)

with open(CWD / "measurements.csv", mode="w") as fp:
    fp.write("array_length,c_timing,python_timing\n")

    for l, c, py in zip(arr_length, c_timings, py_timings):
        fp.write(f"{l},{c},{py}\n")
