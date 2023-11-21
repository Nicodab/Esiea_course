import java.net.*;
import java.io.*;

class HelloServer1 {
    public static void main(String argv[]) throws Exception
    {
        //On installe le combine sur le numero de telephone
        ServerSocket serversocket = new ServerSocket(1111);
        System.out.println("Serveur HTTP démarré sur le port 1111...");

        while (true) {
            //On attend les appels entrants
            Socket socket = serversocket.accept();
            handleRequest(socket);
        }
    }
    
    static void handleRequest(Socket socket){
        try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             OutputStream out = socket.getOutputStream()) {
        
            String request = in.readLine(); // Lecture de la première ligne de la requête HTTP (la ligne de demande) --> Ligne avec la méthode (GET, POST, etc.), le chemin et la version HTTP.
            String host = in.readLine(); // Lecture du host

            if (request != null && host != null) {
                String[] parts = request.split(" ");
                // Divise la ligne de demande en parties en utilisant l'espace comme séparateur.
                // --> [méthode, chemin, version].
                System.out.println("Requête client: " + request);
                System.out.println("Host Client:" + host);

                if (parts.length == 3 && parts[0].equals("GET")) {
                    // Vérifie que la méthode est "GET" et qu'il y a 3 parties dans la ligne de demande.


                    String path = parts[1];
                    // Récupère le chemin à partir des parties de la ligne de demande.
                    int extensionIndex = path.lastIndexOf("."); // Récupère l'extension de fichier
                    String fileExtension = path.substring(extensionIndex + 1);     
                    
                    // GET html
                    if (fileExtension.equals("html")) {
                        File file = new File(path.substring(1));
                        // Crée un objet File pour représenter le fichier "example.html" dans le répertoire courant.
    
                        if (file.exists()) {
                            FileInputStream fis = new FileInputStream(file);
                            // Si le fichier existe, ouvre un flux d'entrée pour le lire.
    
                            out.write("HTTP/1.1 200 OK\r\n".getBytes());
                            out.write("Server: JavaHTTPServer\r\n".getBytes());
                            out.write("Content-Type: text/html\r\n".getBytes());
                            out.write(("Content-Length: " + file.length() + "\r\n").getBytes());
                            out.write("\r\n".getBytes());
                            // Envoi de la ligne de statut HTTP, des en-têtes et du contenu du fichier
    
                            byte[] buffer = new byte[8192];
                            int bytesRead;
                            while ((bytesRead = fis.read(buffer)) != -1) {
                                out.write(buffer, 0, bytesRead);
                            }
                            fis.close(); // Lecture du contenu du fichier en morceaux et l'écrit dans le flux de sortie.
                        } else {
                            // Si le fichier n'existe pas, renvoie une réponse 404 avec un message "Fichier non trouvé".
                            String response = "Fichier non trouvé\n";
                            out.write("HTTP/1.1 404 Not Found\r\n".getBytes());
                            out.write("Server: SimpleHTTPServer\r\n".getBytes());
                            out.write("Content-Type: text/plain\r\n".getBytes());
                            out.write(("Content-Length: " + response.length() + "\r\n").getBytes());
                            out.write("\r\n".getBytes());
                            out.write(response.getBytes());
                        }
                    }
                    else if (fileExtension.equals("pdf")) {
                        // Crée un objet File pour représenter le fichier "example.pdf" dans le répertoire courant.
                        File pdfFile = new File(path.substring(1));

                        if (pdfFile.exists()) {
                            // Si le fichier existe, ouvre un flux d'entrée pour le lire.
                            FileInputStream fis = new FileInputStream(pdfFile);
    
                            // Envoi de la ligne de statut HTTP, des en-têtes et du contenu du fichier
                            out.write("HTTP/1.1 200 OK\r\n".getBytes());
                            out.write("Server: JavaHTTPServer\r\n".getBytes());
                            out.write("Content-Type: application/pdf\r\n".getBytes());
                            out.write(("Content-Length: " + pdfFile.length() + "\r\n").getBytes());
                            out.write("\r\n".getBytes());
    
                            // Lecture du contenu du fichier en morceaux + écriture dans le flux de sortie.
                            byte[] buffer = new byte[8192];
                            int bytesRead;
                            while ((bytesRead = fis.read(buffer)) != -1) {
                                out.write(buffer, 0, bytesRead);
                            }
                            fis.close();
                        } else {
                            // Si le fichier n'existe pas
                            String response = "Fichier PDF non trouvé\n";
                            out.write("HTTP/1.1 404 Not Found\r\n".getBytes());
                            out.write("Server: SimpleHTTPServer\r\n".getBytes());
                            out.write("Content-Type: text/plain\r\n".getBytes());
                            out.write(("Content-Length: " + response.length() + "\r\n").getBytes());
                            out.write("\r\n".getBytes());
                            out.write(response.getBytes());
                            
                        }
                    }
                    else {
                        // Réponse par défaut pour les autres chemins.
                        String response = "Bienvenue sur le serveur Java HTTP !";
                        out.write("HTTP/1.1 200 OK\r\n".getBytes());
                        out.write("Server: JavaHTTPServer\r\n".getBytes());
                        out.write("Content-Type: text/plain\r\n".getBytes());
                        out.write(("Content-Length: " + response.length() + "\r\n").getBytes());
                        out.write("\r\n".getBytes());
                        out.write(response.getBytes());
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

