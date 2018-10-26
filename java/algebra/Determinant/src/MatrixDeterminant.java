
/**
 * https://www.codewars.com/kata/matrix-determinant/train/java
 * DONE
 * */

public class MatrixDeterminant {


    public static final int matrix[][][] = {
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

    private static void print(double matrix [][]) {
        System.out.printf("{");
        for (int i = 0; i < matrix.length ; i++) {
            System.out.printf(i > 0 ? ",{" : "{");
            for (int j = 0; j < matrix[i].length ; j++) {
                System.out.printf(j == 0 ? "%f" : ", %f", matrix[i][j]);
            }
            System.out.printf("}");
            System.out.println("");
        }
        System.out.println("}");
    }

    private static double calc(double matrix[][]) {
        double det = 1;
        int limit = matrix.length;
        for (int i = 0; i < limit ; i++) {
            int gIdx = i;
            for (int j = i+1; j < limit ; j++) {
                if (Math.abs(matrix[j][i]) > Math.abs(matrix[gIdx][i]))
                    gIdx = j;
            }
            if (gIdx != i) {
                swapLines(matrix, i, gIdx);
                det = -det;
            }
            for (int j = i+1; j < limit ; j++) {
                double factor = matrix[i][i] != 0 ? matrix[j][i]  / matrix[i][i] : 0;
                for (int k = i+1; k < limit; k++) {
                    matrix[j][k]= matrix[j][k] - matrix[i][k] * factor;
                }
                matrix[j][i] = 0;
            }
            det *= matrix[i][i];
        }
        return det;
    }

    public static int determinant(int[][] matrix) {
        double mat[][] = new double[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length ; i++) {
            for (int j = 0; j < matrix[i].length ; j++) {
                mat[i][j] = matrix[i][j];
            }
        }
        print(mat);
        return (int) Math.round(calc(mat));
    }

    public static void main(String[] args) {
        System.out.printf("%d\n", determinant(matrix[4]));
    }
}
