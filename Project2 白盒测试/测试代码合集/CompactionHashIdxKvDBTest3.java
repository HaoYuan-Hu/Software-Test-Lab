package com.fantasy.kvdatabase.db;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.io.IOException;
import java.lang.reflect.Method;
import java.util.Deque;


public class CompactionHashIdxKvDBTest3 {
    private static CompactionHashIdxKvDB compactionHashIdxKvDB;

    @Before
    public void createBD() throws IOException {
        compactionHashIdxKvDB = new CompactionHashIdxKvDB();

    }

    @Test
    public void testGet() {
        System.out.println(compactionHashIdxKvDB.get(String.valueOf(35)));
        System.out.println(compactionHashIdxKvDB.get(String.valueOf(8)));
        System.out.println(compactionHashIdxKvDB.get(String.valueOf(52)));
    }

    @Test
    public void testSet() throws InterruptedException, IOException {

        for (int i = 41; i < 55; ++i) {
            compactionHashIdxKvDB.set(String.valueOf(i), String.valueOf(i + 1));
        }
        // Thread.sleep(120 * 1000);
    }


    @After
    public void closeDB() {
        compactionHashIdxKvDB.close();
    }
}
