

public class paintFence{
	public static void main(String[] args) {
		System.out.println(numWays(2,3));
	}

	public static int numWays(int n, int k){
		if (n==0) return 0;
		if (n==1) return k;
		int[] same = new int[n+1];
		int[] diff = new int[n+1];
		same[2] = k;
		diff[2] = k*(k-1);
		for (int i=3; i<=n; i++){
			same[i] = diff[i-1];
			diff[i] = same[i-1]*(k-1) + diff[i-1]*(k-1);
		}
		return diff[n] + same[n];
	}
}
