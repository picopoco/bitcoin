package kr.gitcoin.rest.model;

import java.io.Serializable;
import java.sql.Timestamp;

import org.codehaus.jackson.annotate.JsonIgnore;

public abstract class GitcoinBaseVo implements Serializable {

  private static final long serialVersionUID = 1956098947706968611L;
  private Timestamp createdAt; // 레코드 생성 시각
  @JsonIgnore
  private Integer createdBy; // 레코드 생성자 아이디
  @JsonIgnore
  private Timestamp updatedAt; // 레코드 수정 시각
  @JsonIgnore
  private Integer updatedBy; // 레코드 수정자 아이디

  public Timestamp getCreatedAt() {
    return createdAt;
  }

  public Integer getCreatedBy() {
    return createdBy;
  }

  public Timestamp getUpdatedAt() {
    return updatedAt;
  }

  public Integer getUpdatedBy() {
    return updatedBy;
  }

  public void setCreatedAt(Timestamp createdAt) {
    this.createdAt = createdAt;
  }

  public void setCreatedBy(Integer createdBy) {
    this.createdBy = createdBy;
  }

  public void setUpdatedAt(Timestamp updatedAt) {
    this.updatedAt = updatedAt;
  }

  public void setUpdatedBy(Integer updatedBy) {
    this.updatedBy = updatedBy;
  }

}
