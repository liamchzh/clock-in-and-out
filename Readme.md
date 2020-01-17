# HiMama Clock in/Clock out

Prototype Demo: https://clock-in-and-out.herokuapp.com/

To facilitate testing, you may use any Email and password combination to sign in.

## Approach
The project includes 2 main components: the backend and the frontend. For the backend I chose Python + Flask-RESTful + MySQL and I used React for the frontend.

My first step was to design RESTful APIs after reading the Application requirements. The RESTful APIs return JSON objects, which can be easily manipulated with Javascript at the frontend. As for the manipulation of resources, I focused on 2 resources: `User` and `Clock Events` according to the requirements.

The details of endpoints and Schema are as follows.

Once the API design was done, the second step was to implement the APIs. For the backend, I used Python + MySQL as my technical stack.

As for the frontend, I focused on implementing 2 pages: Login page and Clock in/Clock out page. The interfaces were made clean and easy to use without excessive elements.

## What can be improved
Due to time constraints, the function of editing / delete clocking events has not been completely developed yet.

If I were given another day, I would continue working on the editing / deleting feature, as well as enhance robustness of the project through adding unit tests, validating request data, polishing UI, etc.

If I were given a month, I would totally reimplement it from scratch, starting from doing a user research and considering all constraints and features, then design UI/UX before diving into coding. All feature will be fully tested before launch.

## Endpoints Design
### Login
```
POST /login
```

### Get user :
```
GET /user
```

### List user clock-events
```
GET /user/<string:user_id>/clock-events
```

### List all clock-events
```
GET /clock-events
```

### Create a clock-events
```
POST /clock-events
```

### Retrieve or modify a clock-events
```
GET /clock-events/<string:event_id>
```
```
PUT /clock-events/<string:event_id>
```
```
DELETE /clock-events/<string:event_id>
```

## MySQL Schema Design
```
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint(20) unsigned NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `salt` varchar(32) NOT NULL,
  `name` varchar(200) NOT NULL CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `gender` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `avatar` varchar(200) NOT NULL DEFAULT '',
  `created_at` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `clock_events`;
CREATE TABLE `clock_events` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `event_type` tinyint(2) NOT NULL,
  `timestamp` datetime NOT NULL,
  `is_deleted` tinyint(1) DEFAULT '0',
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
