Schema Design

How to go about the Low Level Design of a System - 

Follow following steps - 
  1. Requirement Gathering - Ask following types of question during req. gathering. (priority order wise)
    a. Impact Design
    b. Impact Implementation
    c. Future Scope.
  2. Class Diagram. ( Relationships and Entities )
  3. Abstract classes and interfaces.
  4. Design Patterns ( Only if there is need for it)
 
 For 1:1 or 1: many relationships, most of the time we use FK, except for the case when, some rows have the relation, other don't. ( the hostel example ).
 
 Steps for drawing ER diags - 
 
 1. Define the entities. ( Nouns. Add adjectives if sub-types ).
 2. Define relationships. Add attributes.
 3. Cardinality
 4. Keys ( Unique by nature, not by data).
 
 Uniqueness constraint. ( enforced by db ).
 
 pk - indexed by default.
 
 Large, unindexable pk. ( need to scan entire db to enforce the uniqueness pk. )
 
 Auto Increment pk - lock for the update queries.
