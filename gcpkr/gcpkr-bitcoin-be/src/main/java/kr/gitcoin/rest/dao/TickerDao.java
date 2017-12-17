package kr.gitcoin.rest.dao;

import java.util.List;

import kr.gitcoin.rest.model.GitcoinCriteria;
import kr.gitcoin.rest.model.TickerVo;

public interface TickerDao {

  public long count(GitcoinCriteria criteria);

  public void create(TickerVo vo);

  public void delete(long timestamp);

  public TickerVo get(long timestamp);

  public List<TickerVo> list(GitcoinCriteria criteria);

  public void update(long timestamp, TickerVo vo);

}
