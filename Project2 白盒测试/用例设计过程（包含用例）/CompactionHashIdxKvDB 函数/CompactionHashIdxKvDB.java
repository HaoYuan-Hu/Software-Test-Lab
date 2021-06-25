public CompactionHashIdxKvDB() {
    this.toCompact = new LinkedList<>();
    this.compactedLevel1 = new LinkedList<>();
    this.compactedLevel2 = new LinkedList<>();
    this.idx = new MultiHashIdx();
    this.toCompactNum = new AtomicInteger(0);
    this.level1Num = new AtomicInteger(0);
    this.level2Num = new AtomicInteger(0);

    loadIdx();

    try {
        compactLevel1();
    } catch (IOException e) {
        e.printStackTrace();
    }
    try {
        compactLevel2();
    } catch (IOException e) {
        e.printStackTrace();
    }
}