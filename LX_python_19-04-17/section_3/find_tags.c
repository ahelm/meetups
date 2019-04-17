#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>
#include <time.h>

void init_array(int *arr1, int *arr2, const int N, int *counter)
{
  for (int i = 0; i < N; i++)
  {
    // propability of 0.5 that both have the same value
    if (rand() / (float)RAND_MAX > 0.5)
    {
      arr1[i] = i + 1;
      arr2[i] = i + 1;
      *counter += 1;
    }
    else
    {
      arr1[i] = i + 1;
      arr2[i] = -1 * (i + 1);
    }
  }
}

void shuffle_array(int *arr, const int N)
{
  if (N > 1)
  {
    int i;
    for (i = 0; i < N - 1; i++)
    {
      int j = i + rand() / (RAND_MAX / (N - i) + 1);
      int t = arr[j];
      arr[j] = arr[i];
      arr[i] = t;
    }
  }
}

int count_common_entries(const int *arr1, const int *arr2, const int N)
{
  int count = 0;
  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      if (arr1[i] == arr2[j])
      {
        count += 1;
        break;
      }
    }
  }
  return count;
}

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
