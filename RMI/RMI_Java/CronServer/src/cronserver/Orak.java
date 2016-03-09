
package cronserver;

import java.util.HashMap;
import java.util.Map;


public class Orak {
     public static void main(String[] args) {
         Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("key1", 30);
        map.put("key2", 40);
        map.put("key3", 50);
        map.put(null, null);

        Map<String, Integer> map2 = new HashMap<String, Integer>();
        map2.put("key3", 10);
        map2.put("key4", 20);
        map2.put("key5", 26);
        map2.put("key6", 22);
        
        Map<String, Integer> map3 = new HashMap<String, Integer>();
//        map3.putAll(map2);
//        map3.putAll(map);
        
        map2.forEach((k, v) -> map.merge(k, v, (v1, v2) -> v1 + v2));
       // map3.forEach((k, v) -> map2.merge(k, v, (v1, v2) -> v1 + v2));
        System.out.println(map2);
     }
}
