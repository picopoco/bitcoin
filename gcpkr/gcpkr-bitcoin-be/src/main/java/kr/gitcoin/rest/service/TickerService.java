package kr.gitcoin.rest.service;

import java.util.List;

import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;

import kr.gitcoin.rest.dao.TickerDao;
import kr.gitcoin.rest.model.GitcoinCriteria;
import kr.gitcoin.rest.model.GitcoinResponseItem;
import kr.gitcoin.rest.model.GitcoinResponseList;
import kr.gitcoin.rest.model.TickerVo;

@Path("/tickers")
public class TickerService {

  private static TickerDao d = null;

  @POST
  @Consumes(MediaType.APPLICATION_JSON)
  public Response create(TickerVo ticker) {
    d.create(ticker);
    return Response.status(200).entity(ticker).build();
  }

  @GET
  @Produces(MediaType.APPLICATION_JSON)
  @Path("/{timestamp}")
  public Response get(@PathParam("timestamp") long timestamp) {
    TickerVo v = d.get(timestamp);
    Status s = v != null ? Status.OK : Status.NO_CONTENT;
    GitcoinResponseItem r = new GitcoinResponseItem();
    r.setResultCode(s.getStatusCode() * 10);
    r.setResultData(v);
    r.setResultMessage(s.name());
    return Response.status(s).entity(r).build();
  }

  @GET
  @Produces(MediaType.APPLICATION_JSON)
  public Response list() {
    GitcoinCriteria c = new GitcoinCriteria();
    List<TickerVo> vs = d.list(c);
    Status s = vs.size() > 0 ? Status.OK : Status.NO_CONTENT;
    GitcoinResponseList r = new GitcoinResponseList();
    r.setResultCode(s.getStatusCode() * 10);
    r.setResultCount(vs.size());
    r.setResultData(vs);
    r.setResultMessage(s.name());
    r.setTotalCount(d.count(c));
    return Response.status(s).entity(r).build();
  }

  public void setTickerDao(TickerDao dao) {
    this.d = dao;
  }

  @PUT
  @Path("{timestamp}")
  @Consumes(MediaType.APPLICATION_JSON)
  @Produces(MediaType.APPLICATION_JSON)
  public Response update(@PathParam("timestamp") long timestamp,
      TickerVo ticker) {
    d.update(timestamp, ticker);
    return Response.status(200).entity(ticker).build();
  }

}
