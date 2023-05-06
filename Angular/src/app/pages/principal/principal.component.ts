import { Component, OnDestroy, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/auth/login.service';
import { User } from 'src/app/services/auth/user';


@Component({
  selector: 'app-principal',
  templateUrl: './principal.component.html',
  styleUrls: ['./principal.component.css']
})

export class PrincipalComponent implements OnInit, OnDestroy{
userLoginOn:boolean=false;
userData?:User;
constructor(private loginService:LoginService){}

ngOnDestroy(): void {
  this.loginService.currentUserData.unsubscribe();
  this.loginService.currentUserLoginOn.unsubscribe();
}


ngOnInit(): void {
  this.loginService.currentUserLoginOn.subscribe({
    next:(userLoginOn)=>{
      this.userLoginOn=this.userLoginOn;
    }
  })

this.loginService.currentUserData.subscribe({
    next:(userData)=>{
      this.userData=userData;
    }

})


}


}
