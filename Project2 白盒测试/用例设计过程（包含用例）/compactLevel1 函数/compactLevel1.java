private void compactLevel1() throws IOException {
    System.out.println("进行Level1 Compact!!!");
    while (!toCompact.isEmpty()) {
        // 创建新的level1 compacted segment file
        // level1的文件命名规则为：filename_level1_num
        LogFile newLogFile = LogFile.create(curLog.path() + "_level1_" + level1Num.getAndIncrement());
        LogFile logFile = toCompact.getFirst();

        /*
            这种情况之下，只可以覆盖同一个logfile内的重复记录，不同的之间依然是可以出现重复的
            */
        idx.allIdxOf(logFile).forEach((key, offset) -> {
            String record = logFile.read(offset);

            final long offset1 = newLogFile.append(record);
            idx.addIdx(newLogFile, key, offset1);
        });

        // 写完后存储到compactedLevel1队列中，并删除toCompact中对应的文件
        compactedLevel1.addLast(newLogFile);
        toCompact.pollFirst();
        deleteLogFile(logFile);
    }
}