package com.fantasy.kvdatabase.db;

import org.junit.*;
import org.junit.rules.ExpectedException;

import java.io.IOException;

public class CompactionHashIdxKvDBTest4 {
    private CompactionHashIdxKvDB compactionHashIdxKvDB;

    @Before
    public void createBD() {

    }

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    @Test
    public void testAN () throws IOException {
        try{ compactionHashIdxKvDB = new CompactionHashIdxKvDB();}
        catch (IndexOutOfBoundsException anIndexOutOfBoundsException){
            thrown.expect(IndexOutOfBoundsException.class);
        }
    }

    @After
    public void closeDB() {
        compactionHashIdxKvDB.close();
    }
}
