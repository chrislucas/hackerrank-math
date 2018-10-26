
import static java.lang.Math.*;

public class DeterminantUsingGaussianElimination {

    public static final double matrix[][][] = {
            {
                {-9, -2, 0, 9, 9, 0, 1}
                , {-7, 5, -9, 6, -1, 5, -9}
                , {6, -8, -6, -8, 5, 4, -7}
                , {3, -10, -9, 9, 2, 7, 3}
                , {-2, 0, 7, -4, -2, 9, 7}
                , {-9, -7, -2, 6, -4, -2, -9}
                , {9, 9, -7, 6, -8, 6, -10}
            }
            , {{1}}
            , {{1, 3}, {2,5}}
            , {{2,5,3}, {1,-2,-1}, {1, 3, 4}}
            , {{2, 4, 5, 3, 1, 2}
                ,{2, 4, 7, 5, 3, 2}
                ,{1, 1, 0, 2, 3, 1}
                ,{1, 3, 9, 0, 3, 2}
                ,{1, 1, 2, 2, 4, 1}
                ,{0, 0, 4, 1, 2, 3}}
    };


    private static void swapLines(double matrix[][], int i, int j) {
        for (int k = 0; k < matrix.length; k++) {
            double temp = matrix[i][k];
            matrix[i][k] = matrix[j][k];
            matrix[j][k] = temp;
        }
    }

    private static double calc(double matrix[][]) {
        double det = 1.0d;
        int limit = matrix.length;
        for (int i = 0; i < limit ; i++) {
            int gIdx = i;
            for (int j = i+1; j < limit ; j++) {
                if ( abs(matrix[j][i]) > abs(matrix[gIdx][i]))
                    gIdx = j;
            }
            if (gIdx != i) {
                swapLines(matrix, i, gIdx);
                det = -det;
            }
            for (int j = i+1; j < limit ; j++) {
                double factor = matrix[i][i] != 0 ? matrix[j][i] / matrix[i][i] : 0;
                for (int k = i+1; k < limit; k++) {
                    matrix[j][k] = matrix[j][k] - matrix[i][k] * factor;
                }
                matrix[j][i] = matrix[j][i] - matrix[i][i] * factor; // matrix[j][i] = 0
            }
            det *= matrix[i][i];
        }
        return det;
    }

    public static void main(String[] args) {
        System.out.printf("%.0f\n", calc(matrix[4]));
    }
}
