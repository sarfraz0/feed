CREATE ROLE alcapone WITH LOGIN ENCRYPTED PASSWORD 'chicago';
CREATE DATABASE accounting OWNER alcapone ENCODING 'UNICODE';

-- after Flask-SQLAlchemy initialization
INSERT INTO users VALUES (1, 'admin', '$6$rounds=40000$ouZ6tmqP9apuUgnz$rRMQWeQ.c15LrA8ebUyp1JwbKLXKwhI1Jc1uopypuiy4PYCA047klMjeGkkx/bqAYQU8i9NvxWH5QQ2UW1qM0.', true); -- password is HRSPAC2+
INSERT INTO personas(user_id, email, valid, last_connected) VALUES (1, 'sarfraz@variablentreprise.com', TRUE, 'TODAY');
INSERT INTO users VALUES (2, 'guest', '$6$rounds=40000$t/kurqCw31EcndqM$pIef7u84N.HEaXVSzlB1JLhvr.YspIFbNWVV6MKhEcLe0LK4faSHyNr0hyNT80YDKMVa5Y7ZEzMte2wo48UX9/', false); -- password is guest
INSERT INTO mailspools VALUES (DEFAULT, 'mail.gandi.net', 587, 'sarfraz@variablentreprise.com', 'sarfraz@variablentreprise.com');
