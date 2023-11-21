
// exemple de Mr.Guyot prof
// C'est le main ici --> On instancie l'obj et on lui passse le paramètre c'est tout (ici c'est en locale en ligne de cmd) 
// Mais ds le main y'a rien
// IL faut un booleen logReplay et un boolen logRecording (on part de log.txt pr les 2). On ne peut pas etre en meme temps en enregistrement et en replay. Le prof fera le replay après le recording et ne testera pas le blindage
import src.PileRPL;

// Pour Lire le Buffer
//import java.io.BufferedInputStream;
import java.io.BufferedReader;
//import java.io.FileReader;
//import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
// Buffer Reader en 
public class CalcUI { // C'est le user qui va manipuler cet obj
// Les args passé vont permettre de récupérer et d'initialiser les flux utilisateurs avec cles args qu'on récupère (ON A QUE LES FLUX d'ENTREES LOCALE OU DISTANT)
// Dans un premiers temps on ne veut que un utilisateur de type unique
    //Exemple de main du prof
    //public static void main(String [] args){ // attr inputUser, OutpUser; loop
        //CaclUI ui = new CaclUI(args);
    //}
    private PileRPL pile;
    private BufferedReader inputUser;
    private PrintStream outputUser;
    private PrintStream outputLog; // log recording pour savoir qd on enregistre maispas la var ici nécessairement OU REVU de session ne serait-ce que pour avoir l'écho de ce qu'on interprète.

    // On peut initialiser la pile au début dans son constructeur comme ca on a déjà son argument
    public CalcUI(String [] args) {
        try{
            initStreams(args); 
            // Initialisation des fluxs (y'en a plusieurs)
            // Boucle for à mettre plutoit dans initStreams d'après le prof (à voir pourquoi)
            mainloop();
        }
            
        catch (Exception e){
            System.out.println("erreur");
        }
            
    }

    // Une sorte de faux main donc c'est pas static
    public void mainloop(){
            while(true){ // while(loop) plus tard, est un booléen qui change en f° des args
                try {
                    // On déclare une pile ici
                    outputUser.println(pile); // Outstream textuel bufferisée pour afficher la pile ou l'état de la pile etc... ça se fait avec la méthode toString redéfinit dans la classe PileRPL
                    String cmd = inputUser.readLine(); // Lecture inputStream du User (pour le moment ce n'est que fait en local) (ajouter l'aide avec le help)
                    //System.out.println("écriture: " + cmd); // pas besoin de cette commande mais permet de voir qu'on récupère bien les commandes du flux d'entrée
                    cmdParser(cmd); //--> Revoir comment faire et définir les différentes commande possible du user (par exemple push, pop, exit et puis les opérateur comme mult, add, div, sub)
                    /// CEST ICI QU'on définit le switch pour la pile en fonction des commandes push etc.
                    // if ("push")

                }
                catch (Exception e){
                    System.out.println(e); // A changer
                }
            }
    }

// FileReader = flux textuel d'entrée bufferisé (revoir avec des vidéos) alors que y'a d'autres types de flux qui sont par caractères ou par bytes.
    public void initStreams(String [] args){
        System.out.println("initStreams\n");

        //String response = inputUser.readLine(); A décommenter !
        // les outputs vont etre initialisé dans chacune des f° ci-dessous
        String argument = args[0];
        try{
                if (argument.equals("user:log")) {
                // Connecter l'utilisateur en mode "log".
                System.out.println("init flux log\n");
            } else if (argument.equals("user:replay")) {
                // Connecter l'utilisateur en mode "replay".
                System.out.println("init flux replay\n");
            } else if (argument.equals("user:local")) {
                // Connecter l'utilisateur en mode "local" | OK
                System.out.println(" init flux locals\n");
                initFullLocal();
            } else if (argument.equals("user:remote")) {
                // Connecter l'utilisateur en mode "local".
                System.out.println("init flux remotes\n");
            }  
            else {
                System.out.println("Argument non reconnu : " + argument);
            }
        }catch (Exception e){
            System.out.println(e); // Pour le mmt on le fait en out.println
        }
        
        
        /*for (int i = 0; i < args.length; i++)
            System.out.println(args[i]);*/ //--> A voir cmt implémenter un for pour lire chaque arg
        
        //initFullLocal();              A CODER
        //initFullRemote();             A CODER
        //initFullReplayLocale();       A CODER
        //initReplayNetwork();          A CODER
    }

    // Initialisation du initFullLocal avec 
    public void initFullLocal() throws Exception {
        inputUser = new BufferedReader(new InputStreamReader(System.in));
        outputUser = System.out;
    }
    public void initFullRemote(){
        inputUser = new BufferedReader(new InputStreamReader(System.in));
        //outputUser = System.out; --> Pas out ici --> faut plutot récupérer le flux de sortie de la requête ... Mais revoir je comprend pas bien 
    }
    public void initFullReplayLocale(){
        
    }
    public void initReplayNetwork(){
        
    }

    public void cmdParser(String cmd){
        if (!cmd.contains("taille")){
            System.out.println(cmd);
        }
        else System.out.println("taille non spécifiée");
    }
}

// Regarder la partier 4 du cours de java pour faire des multi user sur le serveur e,n remote