
    ip : any;
    ngOnInit() {
        console.log(this.el.nativeElement, this.el.nativeElement.component, this.vr.element.nativeElement.parentElement);
        console.log(document.parentElement);
        console.log(document.parentNode);
        console.log(document.getElementsByTagName('ngx-support-chat')[0]);
        this.ip = this.el.nativeElement.parentElement.style.padding; // store initial padding
        // document.parentElement.style.padding = '0 !important';
        this.vr.element.nativeElement.parentElement.style.padding = '0';
        // document.getElementsByTagName('ngx-support-chat')[0].parentNode;
        // this.vr.element.nativeElement.parentElement.style.padding = 0;
    }
    ngOnDestroy(): void {
        console.log('destroy called');
        this.vr.element.nativeElement.parentElement.style.padding = this.ip;

    }
    
    // Method 2 Using css
        /deep/ :host .layout-container .content .columns nb-layout-column {
       padding: 0 !important;
       background: crimson !important;
    }
     .my-component {
        padding: 0;
    }

    :host-context(.my-component) {
        padding: 0 !important;
    }
    :host-context(.columns) {
        padding: 0 !important;
    }
    
    // Method 3
    <app-parent class="parent">
    </app-parent>
    In child.component.scss
    .parent {
    // my custom style
    }
    and in child.component.ts
    encapsulation: ViewEncapsulation.None
    
    // Refer https://stackoverflow.com/questions/58829298/how-to-modify-parent-components-css-property-from-child-component-in-angular/58829895#58829895
