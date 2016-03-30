package messagequeue;

import com.rabbitmq.client.*;
import java.io.IOException;
import java.util.*;
import java.io.*;

public class Worker {

  private static final String TASK_QUEUE_NAME = "task_queue";
  
  private static void doWork(String task) {
    for (char ch : task.toCharArray()) {
      if (ch == '.') {
        try {
          Thread.sleep(1000);
        } catch (InterruptedException _ignored) {
          Thread.currentThread().interrupt();
        }
      }
    }
  }

  public static void main(String[] argv) throws Exception {
    CronDecodeInterface c = new CronImplementation();
    ConnectionFactory factory = new ConnectionFactory();
    factory.setHost("localhost");
    final Connection connection = factory.newConnection();
    final Channel channel = connection.createChannel();

    channel.queueDeclare(TASK_QUEUE_NAME, true, false, false, null);
    System.out.println(" [*] Waiting for messages. To exit press CTRL+C");

    channel.basicQos(1);

    final Consumer consumer = new DefaultConsumer(channel) {
      @Override
      public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
        ByteArrayInputStream bais = new ByteArrayInputStream(body);
        DataInputStream in = new DataInputStream(bais);
        ArrayList<String> dbEvent = new ArrayList();
        while (in.available() > 0) {
            String element = in.readUTF();
            dbEvent.add(element);
        }
        Map<String, Integer> seussCount = c.countEvent(dbEvent);
        Map<String, Integer> sortedMap = c.sortByComparator(seussCount);
        
        ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
        ObjectOutputStream out = new ObjectOutputStream(byteOut);
        out.writeObject(sortedMap);
        byte[] b = byteOut.toByteArray();
        channel.basicPublish("", TASK_QUEUE_NAME,
                            MessageProperties.PERSISTENT_TEXT_PLAIN,
                            b);
      }
    };
    channel.basicConsume(TASK_QUEUE_NAME, false, consumer);
  }
}