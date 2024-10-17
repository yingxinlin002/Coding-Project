

public class QuickSort {

	public static void quicksortMedianOf3(int[] array, int n) {
		quicksortMedianOf3(array, 0, n - 1);
	}

	public static void quicksortRandom(int[] array, int n) {
		quicksortRandom(array, 0, n - 1);
	}

	private static void quicksortMedianOf3(int[] array, int left, int right) { // complete this function
		if (left < right) {
			int pivotIndex = Partition.generateMedianOf3Pivot(array, left, right);
			int[] partitionIndex = Partition.partition(array, left, right, pivotIndex);
			quicksortRandom(array, left, partitionIndex[0] - 1);
			quicksortRandom(array, partitionIndex[1] + 1, right);
		}
	}

	private static void quicksortRandom(int[] array, int left, int right) { // complete this function
		if (left < right) {
			int pivotIndex = Partition.generateRandomPivot(array, left, right);
			int[] partitionIndex = Partition.partition(array, left, right, pivotIndex);
			quicksortRandom(array, left, partitionIndex[0] - 1);
			quicksortRandom(array, partitionIndex[1] + 1, right);
		}
	}
}