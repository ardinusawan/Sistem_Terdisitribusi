
package cronimplementation;

import icron.CronDecodeInterface;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class CronImplementation extends UnicastRemoteObject implements CronDecodeInterface{

    public CronImplementation () throws RemoteException{  }

    public ArrayList<String> readFile1(File fin) throws IOException, RemoteException {
        ArrayList<String> dbEvent = new ArrayList<String>();
        System.out.println("File "+fin.toString()+" accepted");
        System.out.println("Processing...");
        FileInputStream fis = new FileInputStream(fin);
        
	BufferedReader br = new BufferedReader(new InputStreamReader(fis));
 
	String line = new String();
	while ((line = br.readLine()) != null) {
                String modLine, modFin;
                modLine = line.substring(22);
                int t2index = modLine.indexOf(":");
                modFin = modLine.substring(t2index+2);
                //System.out.println("ModFin: " + modFin);
                dbEvent.add(modFin);
	}
	br.close();
        System.out.println("Sorted file "+fin.toString());
        return dbEvent;
    }

    public Map<String, Integer> sortByComparator(Map<String, Integer> unsortMap) throws RemoteException {
        // Convert Map to List
		List<Map.Entry<String, Integer>> list = 
			new LinkedList<Map.Entry<String, Integer>>(unsortMap.entrySet());

		// Sort list with comparator, to compare the Map values
		Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
			public int compare(Map.Entry<String, Integer> o1,
                                           Map.Entry<String, Integer> o2) {
				return (o1.getValue()).compareTo(o2.getValue());
			}
		});
                Collections.reverse(list);
		// Convert sorted map back to a Map
		Map<String, Integer> sortedMap = new LinkedHashMap<String, Integer>();
		for (Iterator<Map.Entry<String, Integer>> it = list.iterator(); it.hasNext();) {
			Map.Entry<String, Integer> entry = it.next();
			sortedMap.put(entry.getKey(), entry.getValue());
		}
		return sortedMap;
                
    }

    public void printMap(Map<String, Integer> map) throws RemoteException {
                int count = 0;
		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			System.out.println(++count + " " +entry.getKey() 
                                      + " --->>" + entry.getValue());
		}
    }
    
}
