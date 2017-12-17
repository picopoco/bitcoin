package kr.gitcoin.rest.model;

public class GitcoinResponseList extends GitcoinResponseItem {

  private static final long serialVersionUID = 958650811010382232L;
  private Integer resultCount;
  private Long totalCount;

  public Integer getResultCount() {
    return resultCount;
  }

  public Long getTotalCount() {
    return totalCount;
  }

  public void setResultCount(Integer resultCount) {
    this.resultCount = resultCount;
  }

  public void setTotalCount(Long totalCount) {
    this.totalCount = totalCount;
  }

}
