package kr.gitcoin.rest.model;

import java.io.Serializable;

public class GitcoinResponseItem implements Serializable {

  private static final long serialVersionUID = 958650811010382232L;
  private Integer resultCode;
  private Object resultData;
  private String resultMessage;

  public Integer getResultCode() {
    return resultCode;
  }

  public Object getResultData() {
    return resultData;
  }

  public String getResultMessage() {
    return resultMessage;
  }

  public void setResultCode(Integer resultCode) {
    this.resultCode = resultCode;
  }

  public void setResultData(Object resultData) {
    this.resultData = resultData;
  }

  public void setResultMessage(String resultMessage) {
    this.resultMessage = resultMessage;
  }

}
