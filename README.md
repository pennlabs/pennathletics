# Penn Athletics Python SDK

Python wrapper around the [Penn Athletics website](http://www.pennathletics.com) to easily access athletics data.

**Note:** This SDK is currently broken due to a website refresh. Stay tuned!

## License

This is published under the MIT license. See [LICENSE](LICENSE).

Setup
-----
* Create new virtualenv
* Install requirements using 'pip install -r requirements.txt'
* Run the Penn Athletics API server using 'python runserver.py'

## Sports

<span name="ids"></span>
### View All Sports (IDs)
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

<span name="years"></span>
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
<td><a href="#ids">View Section on Sport IDs</a></td>
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
<td><a href="#ids">View Section on Sport IDs</a></td>
</tr>
<tr>
<td>Supported Years</td>
<td><a href="#years">View Section on years</a></td>
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
<td><a href="#ids">View Section on Sport IDs</a></td>
</tr>
<tr>
<td>Supported Years</td>
<td><a href="#years">View Section on years</a></td>
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
<td><a href="#ids">View Section on Sport IDs</a></td>
</tr>
<tr>
<td>Supported Years</td>
<td><a href="#years">View Section on years</a></td>
</tr>
<tr>
<td>Response Formats</td>
<td>JSON</td>
</tr>
</table>
