public void set(String key, String value) {

    // 如果当前LogFile写满了，则放到toCompact队列中，并创建新的LogFile
    if (curLog.size() >= MAX_LOG_SIZE_BYTE) {
        String curPath = curLog.path();  // 可以新增写的文件
        Map<String, Long> oldIdx = idx.allIdxOf(curLog);
        curLog.renameTo(curPath + "_" + toCompactNum.getAndIncrement());
        toCompact.addLast(curLog);
        // 创建新的文件后，索引也要更新
        idx.addAllIdx(curLog, oldIdx);
        curLog = LogFile.create(curPath);
        idx.cleanIdx(curLog);
    }

    final String record = Util.composeRecord(key, value);
    idx.addIdx(curLog, key, curLog.append(record));
}