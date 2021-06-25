public String get(String key) {
    // 第一步：从当前的LogFile查找
    if (idx.idxOf(curLog, key) != -1) {
        long offset = idx.idxOf(curLog, key);

        System.out.println(String.format("在当前logfile找到 %s", key));
        return Util.valueOf(curLog.read(offset));
    }

    // 第二步：从toCompact中查找
    String value = find(key, toCompact);
    if (!value.isEmpty()) {
        System.out.println(String.format("在toCompact中找到 %s", key));
        return value;
    }

    // 第三步：从 compactedLevel1 中查找
    value = find(key, compactedLevel1);
    if (!value.isEmpty()) {
        System.out.println(String.format("在compactedLevel1中找到 %s", key));
        return value;
    }

    // 第四步：从 compactedLevel2 中查找
    value = find(key, compactedLevel2);
    if (!value.isEmpty()) {
        System.out.println(String.format("在compactedLevel2中找到 %s", key));
        return value;
    }

    System.out.println(String.format("找不到 %s", key));
    return "";
}