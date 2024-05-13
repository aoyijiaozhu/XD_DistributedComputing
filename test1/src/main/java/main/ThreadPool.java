package main;

import java.io.*;
import java.net.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import main.ServerThread;
public class ThreadPool {
    public static void main(String[] args) throws Exception {
        ServerSocket listenSocket = new ServerSocket(8189);
        Socket socket = null;
        ExecutorService executorService = Executors.newFixedThreadPool(5);
        int count = 0;
        System.out.println("Server listening at 8189");

        while (true) {
            socket = listenSocket.accept();
            count++;
            System.out.println("The total number of clients is " + count + ".");
            executorService.submit(new ServerThread(socket, count));
        }
    }
}