long now(){
    struct timeval time;
    gettimeofday(&time, NULL);
    return time.tv_sec;
}
std::mutex mtx;

class HitCounter{

    deque<pair<int, int> >hits;

    void prune(){
        mtx.lock();
        auto old=upper_bound(hits.begin(), hits.end(), make_pair(now()-300), -1));

        if(old!=hits.end()){
            hits.erase(hits.begin(), old);
        }
        mtx.unlock();

    }
    void hit(){
        mutex.lock();
        if(hits.size()==0){
            hits.push_back(make_pair(now(), 1));
        }else{
            if(now()==hits.back()->first)
                hits.back()->second ++;
            else
                hits.push_back(make_pair(now(), 1));
        }
        mutex.unlock();
        prune();

    }

    int getLog(){
        mutex.lock();
        auto before = lower_bound(hits.begin(), hits.end(), make_pair(now()-300), -1));
        if(before == hits.end()){
            mutex.unlock();
            return 0;
        }


        int sum=0;
        for(auto it=before; it!=hits.end(); it++){
            sum+=it->second;
        }
        mutex.unlock();
        return sum;
    }

};
