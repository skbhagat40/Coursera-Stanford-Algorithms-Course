Scaling the storage layer - 

Cold store db - to store data which is not used frequently (older / stale data). Less compute power / more / cheaper storage.

If data exceeds the db storage limit - we can shard the data using ( Consistent Hashing).

Scaling a read heavy system - Inside a shard - We can have master slave replication. All writes done on master, slaves for reads.

Propagating writes to slaves - 
  a. Online propagation - Wait for all slaves to write data before returning success response to the client.
  Pros - High consistency. Less Read latency.
  Cons - High read latency. Unavailable if a slave goes down. More burden on Slaves.
  
  b. Lazy propagation - Don't weight for slaves response. Have a background job, that batches pending writes.
  Pros - Less Latency, More available. Less load on slaves (because of batched writes).
  Cons - Inconsistency. Data is lost if master goes down and the change is not propagated to slaves properly.
  
  c. Quorum - Hybrid of above two approaches. Wait for successful response from N/2 of slaves. Cross communication between slaves/slaves and master / slaves. So, they 
  mutually update their data.
  Pros - 
  No loss of data if master goes down. Slave with most recent writes becomes the master. If a slave goes down, when it comes up, it will sync with others to update itself.
  Cons - 
  Data inconsistency.
  
  Write Heavy Read Super Heavy - Multi master multi slave systems.
  
  Write Heavy - Multi master system.
  
  Other Appraoch To scale storage - Federated data systems. ( e.g Uber Eats vs Cab) Complex to implement coz of aggregation.
