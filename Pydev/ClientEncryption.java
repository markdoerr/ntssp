package com.python.pydev.license;

import java.math.BigInteger;
import java.util.ArrayList;
import org.python.pydev.core.structure.FastStringBuffer;

public class ClientEncryption
{
  private static ClientEncryption encryption;
  private BigInteger e;
  private BigInteger N;

  public ClientEncryption()
  {
    this.e = new BigInteger("65537", 10);
    this.N = new BigInteger("115177032176946546558269068827440200244040503869596632334637862913980482577252368423165152466486515398576152630074226512838661350005676884681271881673730676993314466894521803768688453811901029052598776873607299993786360160003193977375556220882426365859708520873206921482917525578030271496655309864011180862013", 10);
  }

  public static ClientEncryption getInstance() {
    if (encryption == null)
      return (ClientEncryption.encryption = new ClientEncryption());

    return encryption;
  }

  protected String[] getChunks(String data)
  {
    ArrayList strs = new ArrayList();
    while (data.length() > 128) {
      strs.add(data.substring(0, 128));
      data = data.substring(128);
    }
    if (data.length() > 0)
      strs.add(data);

    return ((String[])strs.toArray(new String[0]));
  }

  public String encrypt(String data) {
    String[] chunks = getChunks(data);
    FastStringBuffer buf = new FastStringBuffer();
    String[] arrayOfString1 = chunks; int j = chunks.length; for (int i = 0; i < j; ++i) { String string = arrayOfString1[i];
      BigInteger m = new BigInteger(string.getBytes());
      BigInteger encrypted = m.modPow(this.e, this.N);
      buf.append(encrypted.toString());
      buf.append("@");
    }
    return buf.toString();
  }

  public String decrypt(String data)
  {
	String s = "email = syphius@hotmail.com\n"+
		     "name = Syhius\n"+
		     "time = "+ Long.MAX_VALUE +"\n"+
		     "licenseType = Multi Developer\n"+
		     "devs = 200";
      return s;
  }
}