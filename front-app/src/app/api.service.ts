import {Injectable} from '@angular/core';
import { Observable } from 'rxjs/observable';
import { HttpClient, HttpClientModule} from '@angular/common/http';
import 'rxjs/add/operator/map';

interface IJumper {
  name: string;
  surname: string;
  nationality: string,
  photo: string
}

@Injectable()
export class ApiService {
  private baseURL = 'http://127.0.0.1:8000'

  constructor(protected httpClient: HttpClient) {}

  public getJumpers(): Observable<any> {
    return this.httpClient.get(`${this.baseURL}/api/v1/jumper/`).map((resp)=>resp);
  }

  public getCompetitions(): Observable<any> {
    return this.httpClient.get(`${this.baseURL}/api/v1/competition/`).map((resp)=>resp);
  }

}
