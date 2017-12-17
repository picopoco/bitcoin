package kr.gitcoin.rest.model;

import java.sql.Timestamp;

import org.codehaus.jackson.annotate.JsonIgnore;

public class TickerVo extends GitcoinBaseVo {

  private static final long serialVersionUID = 7907684310800177798L;
  private float closed;
  @JsonIgnore
  private Timestamp createdAt;
  private float high;
  private float low;
  private float open;
  private long timestamp;
  private float volume;

  public float getClosed() {
    return closed;
  }

  public float getHigh() {
    return high;
  }

  public float getLow() {
    return low;
  }

  public float getOpen() {
    return open;
  }

  public long getTimestamp() {
    return timestamp;
  }

  public float getVolume() {
    return volume;
  }

  public void setClosed(float closed) {
    this.closed = closed;
  }

  public void setHigh(float high) {
    this.high = high;
  }

  public void setLow(float low) {
    this.low = low;
  }

  public void setOpen(float open) {
    this.open = open;
  }

  public void setTimestamp(long timestamp) {
    this.timestamp = timestamp;
  }

  public void setVolume(float volume) {
    this.volume = volume;
  }

}
