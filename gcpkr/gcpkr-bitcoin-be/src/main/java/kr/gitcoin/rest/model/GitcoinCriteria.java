package kr.gitcoin.rest.model;

public class GitcoinCriteria extends GitcoinBaseVo {

  private static final long serialVersionUID = 7634933255847251199L;
  private int limit = 15;
  private long offset = 0L;
  private Long timestampStart;
  private Long timestampStop;

  public int getLimit() {
    return limit;
  }

  public long getOffset() {
    return offset;
  }

  public Long getTimestampStart() {
    return timestampStart;
  }

  public Long getTimestampStop() {
    return timestampStop;
  }

  public void setLimit(int limit) {
    this.limit = limit;
  }

  public void setOffset(long offset) {
    this.offset = offset;
  }

  public void setTimestampStart(Long timestampStart) {
    this.timestampStart = timestampStart;
  }

  public void setTimestampStop(Long timestampStop) {
    this.timestampStop = timestampStop;
  }

}
