
import java.util.Random;

public class Partition {
	
	static Random rand = new Random(System.currentTimeMillis());
	
	protected static void swap(int[] array, int x, int y) {
		int temp = array[x];
		array[x] = array[y];
		array[y] = temp;
	}
	
	public static int generateRandomPivot(int[] array, int left, int right) {
		return left + rand.nextInt(right - left + 1);
	}
	
	public static int generateMedianOf3Pivot(int[] array, int left, int right) {
		int mid = left + (right - left) / 2;
		
		if (array[left] > array[mid])
			swap(array, left, mid);
		if (array[left] > array[right])
			swap(array, left, right);
		if (array[mid] > array[right])
			swap(array, mid, right);
		
		return mid;
	}
	
	public static int[] partition(int[] array, int left, int right, int pivotIndex) {
		int i = left, lowerPartitionIndex = left, upperPartitionIndex = right;
		int pivot = array[pivotIndex];
		
		while(i <= upperPartitionIndex) {
			if (array[i] < pivot) {
				swap(array, lowerPartitionIndex, i);
				i++;
				lowerPartitionIndex++;
			}
			else if (array[i] > pivot) {
				swap(array, upperPartitionIndex, i);
				upperPartitionIndex--;
			}
			else
				i++;
		}
		
		int[] result = new int[2];
		result[0] = lowerPartitionIndex;
		result[1] = upperPartitionIndex;
		
		return result;
	}

}
