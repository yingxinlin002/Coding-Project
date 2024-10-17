
import java.util.Arrays;

public class demo {

	private static void testSorting(int array[], int n) throws Exception {
		int temp[] = new int[n];

		System.out.println("Original array:                  " + Arrays.toString(array));

		for (int i = 0; i < n; i++)
			temp[i] = array[i];
		new MergeSort(temp, n).mergesort();
		System.out.println("MergeSorted array:               " + Arrays.toString(temp));

		for (int i = 0; i < n; i++)
			temp[i] = array[i];
		QuickSort.quicksortMedianOf3(temp, n);
		System.out.println("QuickSorted (median of 3) array: " + Arrays.toString(temp));

		for (int i = 0; i < n; i++)
			temp[i] = array[i];
		QuickSort.quicksortRandom(temp, n);
		System.out.println("QuickSorted (random) array:      " + Arrays.toString(temp));

		for (int i = 0; i < n; i++)
			temp[i] = array[i];
		RadixSort.radixSort(temp, n);
		System.out.println("RadixSorted array:               " + Arrays.toString(temp));
	}

	private static void testSelection(int array[], int n) throws Exception {
		int mergeArray[] = new int[n];
		
		for (int i = 0; i < n; i++)
			mergeArray[i] = array[i];
		new MergeSort(mergeArray, n).mergesort();

		System.out.println("*** Randomized Quick-select ***\n");

		int selArray[] = new int[n];
		for (int k = 1; k <= n; k++) {
			for (int j = 0; j < n; j++)
				selArray[j] = array[j];
			int answer = Selection.select(selArray, n, k);
			System.out.printf(k + "th smallest: %d", selArray[answer]);
			if (selArray[answer] != mergeArray[k - 1])
				System.out.print("; Selection code does not work for k = " + k);
			System.out.println();
		}

		System.out.println("\n*** Median of Medians Quick-select ***\n");

		for (int k = 1; k <= n; k++) {
			for (int j = 0; j < n; j++)
				selArray[j] = array[j];
			int answer = MedianOfMedians.select(selArray, n, k);
			System.out.printf(k + "th smallest: %d", selArray[answer]);
			if (selArray[answer] != mergeArray[k - 1])
				System.out.print("; Median of Medians code does not work for k = " + k);
			System.out.println();
		}
	}

	private static void testPartition() {
		System.out.println("****************** Two-Index Partition with Duplicates ******************\n");
		final int array[] = { -13, -174, 19, 1, 4, 12, 100, 7, 4, 4, 10, 12, 4, 5, 6, 7, 100, 56, 67, 13, 12, 45, 4, 4,
				44, 8, 4, -10, 14, 4, -1, 97, -1009, 4210, 4, 4, 1, 9, 17, 45, 4, -99, -845, -90, -9, 13, -13 };
		int n = array.length;
		System.out.println("Original Array: " + Arrays.toString(array));
		int pivotIndex = 4;
		System.out.println("\npivot = " + array[pivotIndex]);
		int[] partitionIndex = Partition.partition(array, 0, n - 1, pivotIndex);
		System.out.println("Lower Partition Index = " + partitionIndex[0]);
		System.out.println("Upper Partition Index = " + partitionIndex[1]);
		System.out.println("\nAfter Partitioning: " + Arrays.toString(array));
	}

	private static void testRandomizedQuickSort() {
		System.out.println("\n****************** Randomized Quick-Sort with Duplicates ******************\n");
		final int array[] = { -13, -174, 19, 1, 4, 12, 100, 7, 4, 4, 10, 12, 4, 5, 6, 7, 100, 56, 67, 13, 12, 45, 4, 4,
				44, 8, 4, -10, 14, 4, -1, 97, -1009, 4210, 4, 4, 1, 9, 17, 45, 4, -99, -845, -90, -9, 13, -13 };
		int n = array.length;
		System.out.println("Original Array: " + Arrays.toString(array));
		QuickSort.quicksortRandom(array, n);
		System.out.println("After Sorting:  " + Arrays.toString(array));
	}

	private static void testMedianOf3QuickSort() {
		System.out.println("\n****************** Median of 3 Quick-Sort with Duplicates ******************\n");
		final int array[] = { -13, -174, 19, 1, 4, 12, 100, 7, 4, 4, 10, 12, 4, 5, 6, 7, 100, 56, 67, 13, 12, 45, 4, 4,
				44, 8, 4, -10, 14, 4, -1, 97, -1009, 4210, 4, 4, 1, 9, 17, 45, 4, -99, -845, -90, -9, 13, -13 };
		int n = array.length;
		System.out.println("Original Array: " + Arrays.toString(array));
		QuickSort.quicksortMedianOf3(array, n);
		System.out.println("After Sorting:  " + Arrays.toString(array));
	}

	private static void testRadixSort() {
		System.out.println("\n****************** Radix-sort with Duplicates ******************\n");
		final int array[] = { -13, -174, 19, 1, 4, 12, 100, 7, 4, 4, 10, 12, 4, 5, 6, 7, 100, 56, 67, 13, 12, 45, 4, 4,
				44, 8, 4, -10, 14, 4, -1, 97, -1009, 4210, 4, 4, 1, 9, 17, 45, 4, -99, -845, -90, -9, 13, -13 };
		int n = array.length;
		System.out.println("Original Array: " + Arrays.toString(array));
		RadixSort.radixSort(array, n);
		System.out.println("After Sorting:  " + Arrays.toString(array));
	}

	private static void testRandomizedSelect() {
		System.out.println("\n****************** Randomized Quick-Select with Duplicates ******************\n");
		final int array[] = { -13, -174, 19, 1, 4, 12, 100, 7, 4, 4, 10, 12, 4, 5, 6, 7, 100, 56, 67, 13, 12, 45, 4, 4,
				44, 8, 4, -10, 14, 4, -1, 97, -1009, 4210, 4, 4, 1, 9, 17, 45, 4, -99, -845, -90, -9, 13, -13 };
		int n = array.length;
		int[] temp = new int[n];
		System.out.println("Original Array: " + Arrays.toString(array));
		for (int k = 1; k <= array.length; k++) {
			for (int i = 0; i < n; i++)
				temp[i] = array[i];
			System.out.printf("%dth smallest number is %d\n", k, temp[Selection.select(temp, n, k)]);
		}
	}

	private static void testMedianOfMediansSelect() {
		System.out.println("\n****************** Median of Medians with Duplicates ******************\n");
		final int array[] = { -13, -174, 19, 1, 4, 12, 100, 7, 4, 4, 10, 12, 4, 5, 6, 7, 100, 56, 67, 13, 12, 45, 4, 4,
				44, 8, 4, -10, 14, 4, -1, 97, -1009, 4210, 4, 4, 1, 9, 17, 45, 4, -99, -845, -90, -9, 13, -13 };
		int n = array.length;
		System.out.println("Original Array: " + Arrays.toString(array));
		int[] temp = new int[n];
		for (int k = 1; k <= array.length; k++) {
			for (int i = 0; i < n; i++)
				temp[i] = array[i];
			System.out.printf("%dth smallest number is %d\n", k, temp[MedianOfMedians.select(temp, n, k)]);
		}
	}


	public static void main(String args[]) throws Exception {
		System.out.println("*** Sorting/Selection Test Without Duplicates ***\n");
		final int sorting[] = { 19, 1, 12, 100, 7, 8, 4, -10, 14, -1, 97, -1009, 4210 };
		int n = sorting.length;
		int selection[] = new int[n];
		for (int i = 0; i < n; i++)
			selection[i] = sorting[i];
		testSorting(sorting, n);
		System.out.println();
		for (int i = 0; i < n; i++)
			sorting[i] = selection[i];
		testSelection(selection, n);
		System.out.println();

		testPartition();
		testRandomizedQuickSort();
		testMedianOf3QuickSort();
		testRadixSort();
		testRandomizedSelect();
		testMedianOfMediansSelect();

	}
}