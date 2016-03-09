
package cronclient;

import icron.CronDecodeInterface;
import java.io.File;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class CronClient {

    public static void main(String[] args) {
        try{
            Registry myReg = LocateRegistry.getRegistry("127.0.0.1",1099);
            CronDecodeInterface c = (CronDecodeInterface)myReg.lookup("mycron");
            
            File dir = new File("E:\\ITS\\KULIAH\\SEMESTER 6\\SISTER\\cron");
            File fin = new File(dir.getCanonicalPath() + File.separator + "cron.2");
            ArrayList<String> dbEvent = c.readFile1(fin);
            
            Map<String, Integer> seussCount = new HashMap<String,Integer>();
            for(String t: dbEvent) {
                Integer i = seussCount.get(t);
                if (i ==  null) {
                    i = 0;
                }
                seussCount.put(t, i + 1);
            }
            
             Map<String, Integer> sortedMap = c.sortByComparator(seussCount);
             c.printMap(sortedMap);
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }
    
}
