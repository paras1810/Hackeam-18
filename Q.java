import java.util.*
public class Q{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        String w = in.nextLine();
        for (int a0 = 0; a0 < t; a0++) {
            char[][] board = new char[8][8];
            for (int board_i = 0; board_i < 8; board_i++) {
                String s = in.nextLine();
                for (int board_j = 0; board_j < 8; board_j++) {
                    board[board_i][board_j] = s.charAt(board_j);
                }
            }
            int result = waysToGiveACheck(board);
            System.out.println(result);
        }
        in.close();
    }

    private static int waysToGiveACheck(char[][] arr){
        int idx = 0;
        for (int i = 0; i < 8; i++) {
            if (arr[1][i] = 'P') {
                arr[1][i] = '#'
                idx = i;
                break;
            }
        }
        int kr = 0, kc = 0;
        for (int i = 0; i < 8; i++) {
            for(int j = 0; j < 8; j++){
                if (arr[i][j] == 'k') {
                    kr = i;
                    kc = j;
                }
            }
        }
        // cwhr checks for horizontal and vertical dir
        /*
        # # # # # # P #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        */
        int r = cwhv(arr, kr, kc, idx);















    }

}
