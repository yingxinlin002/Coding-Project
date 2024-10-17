
import java.util.Arrays;

public class RadixSort {
	
	private static void countSortOnDigits(int A[], int n, int digits[]) { // complete this function
		int[] C = new int[n];
		Arrays.fill(C, 0);
		int[] T = new int[n];
		
		for (int i = 0; i <= n-1; i++)
			C[digits[i]]++;
		
		for (int i = 1; i <= n-1; i++)
			C[i] += C[i-1];
		
		for (int i = n-1; i >= 0; i--) {
			C[digits[i]]--;
			T[C[digits[i]]] = A[i];
		}
		
		for (int i = 0; i < A.length; i++) {
			A[i] = T[i];
		}
		
	}

	private static void radixSortNonNeg(int A[], int n) { // complete this function
		int M = Arrays.stream(A).max().getAsInt();
		int[] digits = new int[n];
		int e = 1;
		while (M/e > 0) {
			for (int i = 0; i <= n-1; i++)
				digits[i] = (A[i]/e)%n;
			countSortOnDigits(A, n, digits);
			e = e * n;
		}
	}

	public static void radixSort(int[] array, int n) { // complete this function
		/*
		 * Approach: Treat negative sign (-) as the most significant 'digit'
		 * radixSortNonNeg(array, n);
		*/
		
		//Count amount of negative
		int negativeCount = 0;
		for (int i = 0; i < n; i++) {
			if (array[i] < 0)
				negativeCount++;
		}
		
		//Store numbers in neg and nonNeg array
		int[] neg = new int[negativeCount];
		int[] nonNeg = new int[n- negativeCount];
		
		for(int i = 0, j= 0, k = 0; i < n; i++) {
			if (array[i] < 0) {
				neg[j] = (-1) * array[i];
				j++;
			}
			else {
				nonNeg[k] = array[i];
				k++;
			}
		}
		
		//sort nonNeg array
		radixSortNonNeg(nonNeg, nonNeg.length);
		//sort neg array
		radixSortNonNeg(neg, neg.length);
		for (int i = 0; i < neg.length; i++)
			neg[i] = (-1) * neg[i];
		
		int k = negativeCount;
		int j = neg.length - 1;
		for (int i = 0; i < Math.max(neg.length, nonNeg.length); i++) {
			//copy neg from end to beginning
			if(j >= 0) {
				array[i] = neg[j];
				j--;
			}
				
			//copy nonNeg from beginning to end
			if (i < nonNeg.length) {
				array[k] = nonNeg[i];
				k++;
			}
		}
		
	}
}