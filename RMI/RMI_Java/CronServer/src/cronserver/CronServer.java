
package cronserver;

import cronimplementation.CronImplementation;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;


public class CronServer {

    
    public static void main(String[] args) {
        try{
            Registry reg = LocateRegistry.createRegistry(1099);
            CronImplementation c = new CronImplementation();
            reg.rebind("mycron", c);
            
            System.out.println("Server is ready...");
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }
    
}
