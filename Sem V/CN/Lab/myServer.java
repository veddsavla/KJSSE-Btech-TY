import java.io.*;  // Import for Input and Output classes
import java.net.*; // Import for Networking classes like Socket and ServerSocket

public class MyServer {
    public static void main(String[] args) {
        try {
            // Create a server socket that listens on port 6666
            ServerSocket ss = new ServerSocket(6666);

            // Accept incoming client connections, establishing the connection with the client
            Socket s = ss.accept();  // This method waits until a client connects
            
            // Create a data input stream to receive data from the client
            DataInputStream dis = new DataInputStream(s.getInputStream());

            // Read the incoming message from the client
            String str = (String) dis.readUTF();

            // Print the received message to the console
            System.out.println("message= " + str);

            // Close the server socket once the communication is over
            ss.close();
        } catch (Exception e) {
            // Handle any exceptions by printing the error message
            System.out.println(e);
        }
    }
}
