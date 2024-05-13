package main;

import java.io.*;
import java.net.Socket;
import java.util.Arrays;
import java.util.regex.Pattern;

public class ServerThread extends Thread implements Runnable {

    Socket socket = null;
    int clientNum = 0;

    public ServerThread(Socket socket, int clientNum) {
        this.socket = socket;
        this.clientNum = clientNum;
    }

    public  double dotProduct(double[][] vector) {
        // 实现向量点乘
        double result = 0;
        for (int i = 0; i < vector[0].length; i++) {
            result += vector[0][i] * vector[1][i];
        }
        return result;
    }
    public  double[] crossProduct(double[][] vector) {
        // 实现向量叉乘
        double[] result = {0,0,0};
        result[0] = vector[0][1] * vector[1][2] - vector[0][2] * vector[1][1];
        result[1] = vector[0][2] * vector[1][0] - vector[0][0] * vector[1][2];
        result[2] = vector[0][0] * vector[1][1] - vector[0][1] * vector[1][0];
        return result;
    }
    public void printArray(double[][] array) {
        // 打印数组，用于测试
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(array[i][j]);
                System.out.print(" ");
            }
            System.out.println("");
        }
    }

    public double[][] parseString(String str) {
        // 解析用户发送的字符串
        // System.out.println("str:"+str);

        // System.out.println("矩阵运算中");
        String[] rows = str.split(","); // 按逗号分隔字符串得到行数组
        // System.out.println("rows:"+Arrays.deepToString(rows));
        double[][] result = new double[rows.length][]; // 创建二维数组，行数为行数组的长度

        for (int i = 0; i < rows.length; i++) {
            String[] elements = rows[i].split(" "); // 按空格分隔每一行的元素

            result[i] = new double[elements.length]; // 创建当前行的一维数组，长度为元素数组的长度

            for (int j = 0; j < elements.length; j++) {
                result[i][j] = Double.parseDouble(elements[j]); // 将元素转换为double类型并存入当前行的数组
            }
        }
        // System.out.println("result: " + Arrays.deepToString(result));
        return result; // 返回二维数组
    }

    public void run() {
        InputStream is = null;
        InputStreamReader isr = null;
        BufferedReader br = null;
        OutputStream os = null;
        PrintWriter pw = null;
        try {
            is = socket.getInputStream();
            isr = new InputStreamReader(is);
            br = new BufferedReader(isr);
            os = socket.getOutputStream();
            pw = new PrintWriter(os);
            String info = null;
            int method = 0;
            while ((info = br.readLine()) != null) {
                System.out.println("Message from client"+clientNum + ",message:" + info);
                if (info.equals("q")) {
                    socket.close();
                    System.exit(0);
                }
                // 判断用户输入的是哪种方式
                else if (info.equals("0")) {
                    method = Integer.parseInt(info);
                    info = "您选择的矩阵计算方式是点乘,请输入点乘的两个数组:";
                    pw.println(info); // 写入输入流
                    pw.flush(); // 向用户发送
                } else if (info.equals("1")) {
                    method = Integer.parseInt(info);
                    info = "您选择的矩阵计算方式是叉乘,请输入叉乘的两个数组:";
                    pw.println(info); // 写入输入流
                    pw.flush(); // 向用户发送
                } else {
                    // 判断用户输入是否符合数组输入结构
                    boolean isValidInput = Pattern.matches("\\d+( \\d+)*,\\d+( \\d+)*", info);
                    if (isValidInput) {
                        double[][] numArray = parseString(info);
                        if (method == 0) {
                            System.out.println("计算点乘中");
                            double result = dotProduct(numArray);
                            info = "点乘结果为:" + result;
                            pw.println(info); // 写入输入流
                            pw.flush(); // 向用户发送
                        } else if (method == 1) {
                            System.out.println("计算叉乘中");
                            double[] result = crossProduct(numArray);
                            info = "叉乘结果为:" + Arrays.toString(result);
                            pw.println(info); // 写入输入流
                            pw.flush(); // 向用户发送
                        }
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (pw != null)
                    pw.close();
                if (os != null)
                    os.close();
                if (br != null)
                    br.close();
                if (isr != null)
                    isr.close();
                if (is != null)
                    is.close();
                if (socket != null)
                    socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
