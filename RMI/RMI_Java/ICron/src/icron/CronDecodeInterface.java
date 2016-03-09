
package icron;

import java.io.File;
import java.io.IOException;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.Map;


public interface CronDecodeInterface extends Remote{
     
    public  ArrayList<String> readFile1(File fin) throws IOException, RemoteException;
    
    public Map<String, Integer> sortByComparator(Map<String, Integer> unsortMap) throws RemoteException;
    
    public void printMap(Map<String, Integer> map) throws RemoteException;
    
}
