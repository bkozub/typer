import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service'

@Component({
  selector: 'type',
  templateUrl: './type.component.html',
  styleUrls: ['./type.component.css'],
  providers: [ApiService]
})
export class TypeComponent implements OnInit {

  private jumpers = [];
  private competitions = [];
  private availableCompetitions = [];

  constructor(private ApiService: ApiService) {}

  ngOnInit(): void {
  
    this.ApiService.getJumpers().subscribe(data=> this.jumpers = data);
    this.ApiService.getCompetitions().subscribe(data=> this.competitions = data);

  }

  private onSelectJumper = (id) => {
    this.availableCompetitions = this.jumpers.filter(elem => elem.pk !== id);
  }

  

}
