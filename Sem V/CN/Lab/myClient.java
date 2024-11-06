import java.io.*;  // Import for Input and Output classes
import java.net.*; // Import for Networking classes like Socket and ServerSocket

public class MyClient {
    public static void main(String[] args) {
        try {
            // Create a socket to connect to the server running on localhost at port 6666
            Socket s = new Socket("localhost", 6666);
            
            // Create an output stream to send data to the server
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            
            // Write a message to the server, "Hello Server"
            dout.writeUTF("Hello Server");
            
            // Flush the output stream to ensure all data is sent
            dout.flush();
            
            // Close the data output stream
            dout.close();
            
            // Close the socket connection
            s.close();
        } catch (Exception e) {
            // Handle any exceptions by printing the error message
            System.out.println(e);
        }
    }
}
