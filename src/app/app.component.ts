import { Component,OnInit, AfterViewInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavComponent } from './nav/nav.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NavComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit, AfterViewInit {
  title = 'projectdcp';
  isLoading = true;
  ngOnInit(): void {
  }
  ngAfterViewInit(): void {
    setTimeout(() => {
      this.isLoading = false; 
    }, 1000); 
  }
}