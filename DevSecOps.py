DevSecOps: Security with DevOps

Hi everyone! I’m back with a new blog where will be discussing a term called DevSecOps. This term directly related to a very important component of technology which is security. So let’s discuss what is DevSecOps? Why it’s so much important? How it comes into the picture?

If we are talking about technologies then the time in which we are currently living is a time of the revolution, a revolution of technologies. Now a days almost everything runs on technology whatever you say shopping, eating, reading, communications, living, etc. More we are getting dependent on the technologies more we are opening us to the world. In fact, It is very good if these technologies are making our life easy, simple and faster unless they don’t harm us. Yes you heard me correct, you know what technologies do make our life simple and fast but they are making us more vulnerable. You must be thinking that how then answer is Data. Data could be anything your bank details, your personal information i.e. your private documents, current location, government secrets, etc. Where data act as fuel for these technologies there are some people use these data as a weapon against you.

For example, if you are owning or using a website or any product which is running over the web used by lots of users and it consists of very critical and personal data which got into wrong hand then it can destroy lots of lives results in loss of business. Here Security plays a vital role and DevSecOps comes into the picture.

What is DevSecOps?
devsecops.png
DevSecOps is a mindset to integrate the security practice into the DevOps process, here the goal is to achieve security while building applications and APIs from end to end. In DevSecOps, two seemingly opposing goals — “speed of delivery” and “secure code” — are merged into one streamlined process. Where DevOps focuses on the continuous development, Operations, and application delivery there DevSecOps focuses on Continuous development, Operations, application delivery, and most important security as well. I’m not trying to differentiate them in fact at the end DevSecOps is part of DevOps only.
Let’s discuss some typical DevOps and DevSecOps workflow:

devsecops-101-14-638
Developers create code using a version control management system.
other developers retrieve the code from the version control management system and carry out analysis of the static code to identify any security defects or bugs in code quality.
An environment is then created, using an iac(infrastructure-as-code) tool, such as terraform. The application is deployed and security configurations are applied to the system.
Automation tests are then executed against the newly deployed application, including back-end, UI, integration, security tests, and API.
If the application passes these tests, it is deployed to a production environment.
This new production environment is monitored continuously to identify any active security threats to the system.
Advantages included in DevSecOps
Greater speed and agility for security teams
An ability to respond to change and needs rapidly
Better collaboration and communication among teams
More opportunities for automated builds and quality assurance testing
Early identification of vulnerabilities in code
Team member assets are freed to work on high-value work
devSecOps
Implementation of DevSecOps
There are various ways of providing security to applications under the roof of DevSecOps i.e. Security over :

Environments: Environment should be protected with proper authorization and authentication.
Data: Proper encryption of the data in the storage and transfer medium.
CI/CD Process: Security scanners for the containers.
Accessibility: There should be the least number of control access and individual user access.
Testing: Automated Security testing should be used.
Networking: Secure and isolated the networking between the services
API Gateways: Ensure secure API gateways.
Policies: Include security policies the secure infrastructure.
To conclude this, I can say only that Security should be one of the major concern and to achieve this DevSecOps practice should be considered from start to end of a project. I hope you got a basic overview of DevSecOps.

Thanks!
