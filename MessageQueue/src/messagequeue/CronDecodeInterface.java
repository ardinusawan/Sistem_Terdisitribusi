
package messagequeue;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;


public interface CronDecodeInterface {
     
    public  void readFile1(File fin, ArrayList<String> dbEvent) throws IOException;
    
    public Map<String, Integer> sortByComparator(Map<String, Integer> unsortMap);
    
    public void printMap(Map<String, Integer> map);
    
    public Map<String, Integer> countEvent(ArrayList<String> dbEvent);
}
