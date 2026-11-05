"""
SCAM SHIELD - Automated GitHub & Vercel Sync Engine
Uses pure Python (dulwich) to stage, commit, and push updates to GitHub.
Once pushed to GitHub, Vercel automatically deploys the updated web application.
"""
import os
import sys
from dulwich.repo import Repo
from dulwich import porcelain

def auto_update(repo_url=None, commit_msg="Release update: SCAM SHIELD upgraded build"):
    print("=" * 65)
    print("  SCAM SHIELD -> Automated GitHub & Vercel Deployment Engine")
    print("=" * 65)

    # 1. Open or initialize repository
    if not os.path.exists(".git"):
        print("[*] Initializing local git repository...")
        repo = Repo.init(".")
    else:
        repo = Repo(".")

    # 2. Stage all source files and clean untracked binaries
    print("[*] Staging source files...")
    porcelain.add(repo, paths=["."])

    # Ensure large binaries, archives, and python caches are not tracked
    index = repo.open_index()
    to_untrack = []
    for entry in index:
        decoded = entry.decode("utf-8", errors="replace").replace("\\", "/")
        if (decoded.endswith(".exe") or decoded.endswith(".zip") or 
            "__pycache__" in decoded or decoded == "live_url.txt"):
            to_untrack.append(decoded)
    if to_untrack:
        porcelain.rm(repo, paths=to_untrack, cached=True)
        print(f"[*] Excluded {len(to_untrack)} binary/cache artifacts from git index.")

    # 3. Create commit
    try:
        commit_id = porcelain.commit(
            repo,
            message=commit_msg.encode("utf-8"),
            author=b"ScamShield Dev <dev@scamshield.ai>"
        )
        print(f"[+] Commit created: {commit_id.decode()[:8]}")
    except Exception as e:
        print(f"[*] Repository status: {e}")

    # 4. Check or configure remote origin
    config = repo.get_config()
    existing_remote = None
    try:
        existing_remote = config.get((b"remote", b"origin"), b"url").decode("utf-8")
        print(f"[*] Found existing remote origin: {existing_remote}")
    except Exception:
        pass

    target_url = repo_url or existing_remote

    if not target_url:
        print("\n[!] No GitHub repository URL is linked yet.")
        print("To push to GitHub and auto-deploy to Vercel, enter your GitHub URL.")
        print("Format: https://github.com/YOUR_USERNAME/YOUR_REPO.git")
        print("Or if using a GitHub Personal Access Token (PAT):")
        print("Format: https://<TOKEN>@github.com/YOUR_USERNAME/YOUR_REPO.git")
        try:
            target_url = input("\nEnter your GitHub repository URL: ").strip()
        except EOFError:
            target_url = None

    if target_url:
        try:
            config.set((b"remote", b"origin"), b"url", target_url.encode("utf-8"))
            config.write_to_path()
            print(f"[+] Configured remote origin: {target_url}")

            # Keep main and master in sync
            head_commit = repo[b"HEAD"]
            repo[b"refs/heads/master"] = head_commit
            repo[b"refs/heads/main"] = head_commit

            print("[*] Pushing latest commit to GitHub...")
            pushed = False
            for branch in [b"refs/heads/main:refs/heads/main", b"refs/heads/master:refs/heads/master"]:
                try:
                    porcelain.push(repo, target_url, refspecs=[branch])
                    print(f"[+] Successfully pushed {branch.decode().split(':')[0]}!")
                    pushed = True
                except Exception as b_err:
                    print(f"[*] Push note for {branch.decode().split(':')[0]}: {b_err}")

            if pushed:
                print("\n" + "=" * 65)
                print("[+] SUCCESS: Pushed to GitHub repository!")
                print("[+] Vercel auto-deploy initiated: Live web application updating...")
                print("=" * 65)
            else:
                print("\n[!] Push failed. Please check your GitHub permissions or PAT token.")
        except Exception as err:
            print(f"\n[!] Push notice: {err}")
            print("\n[Tip] If authentication failed, use a GitHub Personal Access Token:")
            print("     https://<TOKEN>@github.com/YOUR_USERNAME/YOUR_REPO.git")
    else:
        print("\n[i] All changes are committed locally.")
        print("    To push to GitHub & Vercel anytime, run:")
        print("    auto_update_github.bat https://github.com/YOUR_USERNAME/YOUR_REPO.git")

if __name__ == "__main__":
    arg_url = sys.argv[1] if len(sys.argv) > 1 else None
    auto_update(repo_url=arg_url)
