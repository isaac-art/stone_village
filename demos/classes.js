
class EventCounter{
    constructor(queryString, threshold, minDuration, minInterval){
        this.queryString = queryString;
        this.threshold = threshold;
        this.minDuration = minDuration;
        this.minInterval = minInterval;
        this.events = [];
        this.started = null;
        this.lastEventOff = null;
    }

    update(e){
        const now = Date.now();
        if(e.score > this.threshold){
            if(this.lastEventOff === null || (now - this.lastEventOff >= this.minInterval)){
                if(this.started === null){ this.started = now; }
            }
        }else {
            if(this.started !==null && (now-this.started >=this.minDuration)){
                let ev = { start: this.started, stop: now };
                this.events.push(ev);
                this.lastEventOff = now;
                this.broadcast(ev);
            }
            this.started = null;
        }
    }

    broadcast(e){ 
        // websocket broadcast this event 
    }

    reset(){
        this.events = [];
        this.started = null;
        this.lastEventOff = null;
    }
}

class Timer{
    constructor(queryString, threshold){
        this.queryString = queryString;
        this.threshold = threshold;
        this.startTime = null;
        this.elapsedTime = 0;
        this.events = [];
    }

    update(e){
        const now = Date.now();
        if(e.score > this.threshold && this.startTime === null){
            this.startTime = now;
        }
        if(e.score <= this.threshold && this.startTime !== null){
            this.elapsedTime += now - this.startTime;
            let ev = { start: this.startTime, stop: now };
            this.events.push(ev);
            this.broadcast(ev);
            this.startTime = null;
        }
    }

    getElapsedTime(){
        if (this.startTime !== null) {
            // include the current duration as well
            return this.elapsedTime + (Date.now() - this.startTime);
        } else {
            return this.elapsedTime;
        }
    }

    broadcast(e){
        // websocket broadcast this event
    };

    reset(){
        this.startTime = null;
        this.elapsedTime = 0;
        this.events = [];
    }

}


export { EventCounter, Timer}