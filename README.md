# Penn Athletics Python SDK

Python wrapper around the [Penn Athletics website](http://www.pennathletics.com) to easily access athletics data.

## License

This is published under the MIT license. See [LICENSE](LICENSE).

Setup
-----
* Install [redis](http://redis.io/)
* Create new virtualenv
* Install requirments using 'pip install -r requirements.txt'
* Run the penn athletics API server using 'python runserver.py'

## Sports

### View All Sports
<table>
<tr>
<td>URL</td>
<td><code>http://api.pennlabs.org/athletics</code></td>
</tr>
<tr>
<td>Response Formats</td>
<td>JSON</td>
</tr>
</table>

### View Available Years
<table>
<tr>
<td>URL</td>
<td><code>http://api.pennlabs.org/athletics/{sportid}</code></td>
</tr>
<tr>
<td>HTTP Methods</td>
<td>GET</td>
</tr>
<tr>
<td>Current Sport ID's</td>
<td>'M_Baseball', 'M_Basketball', 'M_Track_Cross', 'M_Fencing', 'M_Football', 'M_Sprint_Football', 'M_Golf', 'M_Lacrosse', 'M_Heavy_Rowing', 'M_Light_Rowing', 'M_Soccer', 'M_Squash', 'M_Swimming', 'M_Tennis', 'M_Wrestling', 'W_Basketball', 'W_Track_Cross', 'W_Fencing', 'W_Hockey', 'W_Golf', 'W_Gymnastics', 'W_Lacrosse', 'W_Rowing', 'W_Soccer', 'W_Softball', 'W_Squash', 'W_Swimming', 'W_Tennis', 'W_Volleyball'</td>
</tr>
<tr>
<td>Response Formats</td>
<td>JSON</td>
</tr>
</table>

## Athletes

### Roster

<table>
<tr>
<td>URL</td>
<td><code>http://api.pennlabs.org/athletics/{sportid}/{year}/roster</code></td>
</tr>
<tr>
<td>HTTP Methods</td>
<td>GET</td>
</tr>
<tr>
<td>Current Sport ID's</td>
<td>'M_Baseball', 'M_Basketball', 'M_Track_Cross', 'M_Fencing', 'M_Football', 'M_Sprint_Football', 'M_Golf', 'M_Lacrosse', 'M_Heavy_Rowing', 'M_Light_Rowing', 'M_Soccer', 'M_Squash', 'M_Swimming', 'M_Tennis', 'M_Wrestling', 'W_Basketball', 'W_Track_Cross', 'W_Fencing', 'W_Hockey', 'W_Golf', 'W_Gymnastics', 'W_Lacrosse', 'W_Rowing', 'W_Soccer', 'W_Softball', 'W_Squash', 'W_Swimming', 'W_Tennis', 'W_Volleyball'</td>
</tr>
<tr>
<td>Supported Years</td>
<td>Refer to Section on Years</td>
</tr>
<tr>
<td>Response Formats</td>
<td>JSON</td>
</tr>
</table>

### Search

<table>
<tr>
<td>URL</td>
<td><code>http://api.pennlabs.org/athletics/{sportid}/{year}</code></td>
</tr>
<tr>
<td>HTTP Methods</td>
<td>GET</td>
</tr>
<tr>
<td>Current Sport ID's</td>
<td>'M_Baseball', 'M_Basketball', 'M_Track_Cross', 'M_Fencing', 'M_Football', 'M_Sprint_Football', 'M_Golf', 'M_Lacrosse', 'M_Heavy_Rowing', 'M_Light_Rowing', 'M_Soccer', 'M_Squash', 'M_Swimming', 'M_Tennis', 'M_Wrestling', 'W_Basketball', 'W_Track_Cross', 'W_Fencing', 'W_Hockey', 'W_Golf', 'W_Gymnastics', 'W_Lacrosse', 'W_Rowing', 'W_Soccer', 'W_Softball', 'W_Squash', 'W_Swimming', 'W_Tennis', 'W_Volleyball'</td>
</tr>
<tr>
<td>Supported Years</td>
<td>Refer to Section on Years</td>
</tr>
<tr>
<td>Parameters</td>
<td>All sports have name & hometown. Looking at a sample roster from each sport will show all available parameters to search by. May search by any number at once.</td>
</tr>
<tr>
<td>Response Formats</td>
<td>JSON</td>
</tr>
</table>

## Schedules

### View Schedule

<table>
<tr>
<td>URL</td>
<td><code>http://api.pennlabs.org/athletics/{sportid}/{year}/schedule</code></td>
</tr>
<tr>
<td>HTTP Methods</td>
<td>GET</td>
</tr>
<tr>
<td>Current Sport ID's</td>
<td>'M_Baseball', 'M_Basketball', 'M_Track_Cross', 'M_Fencing', 'M_Football', 'M_Sprint_Football', 'M_Golf', 'M_Lacrosse', 'M_Heavy_Rowing', 'M_Light_Rowing', 'M_Soccer', 'M_Squash', 'M_Swimming', 'M_Tennis', 'M_Wrestling', 'W_Basketball', 'W_Track_Cross', 'W_Fencing', 'W_Hockey', 'W_Golf', 'W_Gymnastics', 'W_Lacrosse', 'W_Rowing', 'W_Soccer', 'W_Softball', 'W_Squash', 'W_Swimming', 'W_Tennis', 'W_Volleyball'</td>
</tr>
<tr>
<td>Supported Years</td>
<td>Refer to Section on Years</td>
</tr>
<tr>
<td>Response Formats</td>
<td>JSON</td>
</tr>
</table>

